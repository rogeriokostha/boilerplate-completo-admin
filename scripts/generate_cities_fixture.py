import json, os, requests

# URL oficial da API do IBGE
URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

# Pasta de fixtures
FIXTURES_DIR = "locations/fixtures"
os.makedirs(FIXTURES_DIR, exist_ok=True)

print("📥 Baixando dados do IBGE...")
response = requests.get(URL)
response.raise_for_status()
data = response.json()

print(f"✅ {len(data)} cidades recebidas. Formatando...")

# Criar lista no formato Django fixture
cities = []
pk_counter = 1

for city in sorted(data, key=lambda x: x["nome"]):
    nome = city["nome"]

    # Detecta a UF, mesmo se microrregião for None
    uf = None
    try:
        uf = city["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    except (TypeError, KeyError):
        try:
            # fallback: estrutura diferente em alguns registros (ex: DF)
            uf = city["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
        except (TypeError, KeyError):
            print(f"⚠️  Não foi possível obter UF para: {city['nome']}")
            continue  # pula o registro problemático

    # Mapa UF -> ID (mesmo PK da fixture states.json)
    state_map = {
        "AC": 1,
        "AL": 2,
        "AP": 3,
        "AM": 4,
        "BA": 5,
        "CE": 6,
        "DF": 7,
        "ES": 8,
        "GO": 9,
        "MA": 10,
        "MT": 11,
        "MS": 12,
        "MG": 13,
        "PA": 14,
        "PB": 15,
        "PR": 16,
        "PE": 17,
        "PI": 18,
        "RJ": 19,
        "RN": 20,
        "RS": 21,
        "RO": 22,
        "RR": 23,
        "SC": 24,
        "SP": 25,
        "SE": 26,
        "TO": 27,
    }

    cities.append(
        {
            "model": "locations.city",
            "pk": pk_counter,
            "fields": {"name": nome, "state": state_map[uf]},
        }
    )
    pk_counter += 1

# Salvar cities.json
output_path = os.path.join(FIXTURES_DIR, "cities.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(cities, f, ensure_ascii=False, indent=2)

print(f"🏙️  cities.json criado com {len(cities)} cidades.")
print(f"📂 Arquivo salvo em: {output_path}")
