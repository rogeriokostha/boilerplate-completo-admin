import os, json, zipfile

# Estrutura de diretórios
fixtures_dir = "locations/fixtures"
os.makedirs(fixtures_dir, exist_ok=True)

# ========================
# 1️⃣ countries.json
# ========================
countries = [
    {"model": "locations.country", "pk": 1, "fields": {"name": "Brasil", "code": "BR"}}
]
with open(os.path.join(fixtures_dir, "countries.json"), "w", encoding="utf-8") as f:
    json.dump(countries, f, ensure_ascii=False, indent=2)

# ========================
# 2️⃣ states.json
# ========================
states = [
    {
        "model": "locations.state",
        "pk": 1,
        "fields": {"name": "Acre", "uf": "AC", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 2,
        "fields": {"name": "Alagoas", "uf": "AL", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 3,
        "fields": {"name": "Amapá", "uf": "AP", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 4,
        "fields": {"name": "Amazonas", "uf": "AM", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 5,
        "fields": {"name": "Bahia", "uf": "BA", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 6,
        "fields": {"name": "Ceará", "uf": "CE", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 7,
        "fields": {"name": "Distrito Federal", "uf": "DF", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 8,
        "fields": {"name": "Espírito Santo", "uf": "ES", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 9,
        "fields": {"name": "Goiás", "uf": "GO", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 10,
        "fields": {"name": "Maranhão", "uf": "MA", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 11,
        "fields": {"name": "Mato Grosso", "uf": "MT", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 12,
        "fields": {"name": "Mato Grosso do Sul", "uf": "MS", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 13,
        "fields": {"name": "Minas Gerais", "uf": "MG", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 14,
        "fields": {"name": "Pará", "uf": "PA", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 15,
        "fields": {"name": "Paraíba", "uf": "PB", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 16,
        "fields": {"name": "Paraná", "uf": "PR", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 17,
        "fields": {"name": "Pernambuco", "uf": "PE", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 18,
        "fields": {"name": "Piauí", "uf": "PI", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 19,
        "fields": {"name": "Rio de Janeiro", "uf": "RJ", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 20,
        "fields": {"name": "Rio Grande do Norte", "uf": "RN", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 21,
        "fields": {"name": "Rio Grande do Sul", "uf": "RS", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 22,
        "fields": {"name": "Rondônia", "uf": "RO", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 23,
        "fields": {"name": "Roraima", "uf": "RR", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 24,
        "fields": {"name": "Santa Catarina", "uf": "SC", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 25,
        "fields": {"name": "São Paulo", "uf": "SP", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 26,
        "fields": {"name": "Sergipe", "uf": "SE", "country": 1},
    },
    {
        "model": "locations.state",
        "pk": 27,
        "fields": {"name": "Tocantins", "uf": "TO", "country": 1},
    },
]
with open(os.path.join(fixtures_dir, "states.json"), "w", encoding="utf-8") as f:
    json.dump(states, f, ensure_ascii=False, indent=2)

# ========================
# 3️⃣ README.txt
# ========================
readme = """=============================
Digitalizador Base - Locations
=============================

Este pacote contém os fixtures oficiais do módulo "locations"
com toda a base geográfica do Brasil, prontos para uso em qualquer
projeto Django compatível com o app `locations`.

------------------------------------------
📁 Estrutura:
------------------------------------------
countries.json  → Contém o país "Brasil"
states.json     → Contém os 27 estados (26 + DF)
cities.json     → Contém as 5.570 cidades brasileiras

------------------------------------------
🧩 Como importar:
------------------------------------------
1. Coloque todos os arquivos em:
   locations/fixtures/

2. Rode:
   python manage.py loaddata locations/fixtures/countries.json
   python manage.py loaddata locations/fixtures/states.json
   python manage.py loaddata locations/fixtures/cities.json

------------------------------------------
📄 Observações:
------------------------------------------
• IDs são sequenciais (não usam código IBGE)
• Dados acentuados corretamente (UTF-8)
• Busca acento-insensível no endpoint de cidades
• Compatível com SQLite, PostgreSQL e MySQL
"""
readme_path = os.path.join(fixtures_dir, "README.txt")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)

# ========================
# 4️⃣ Compacta os arquivos existentes
# ========================
zip_filename = "locations_fixtures_brasil.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file in ["countries.json", "states.json", "README.txt"]:
        zipf.write(os.path.join(fixtures_dir, file), arcname=file)

print(f"✅ Pacote gerado: {zip_filename}")
print(
    "➡️ Coloque o cities.json na pasta fixtures e compacte novamente se quiser incluir."
)
