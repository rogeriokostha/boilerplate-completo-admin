import zipfile
import os

zip_filename = "locations_fixtures_brasil.zip"
cities_path = "locations/fixtures/cities.json"

if not os.path.exists(zip_filename):
    print("❌ Arquivo ZIP não encontrado.")
    exit()

if not os.path.exists(cities_path):
    print("❌ cities.json não encontrado em locations/fixtures/.")
    exit()

with zipfile.ZipFile(zip_filename, "a", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(cities_path, arcname="cities.json")

print("✅ cities.json adicionado ao ZIP com sucesso!")
print(f"📦 Arquivo final: {zip_filename}")
