=============================
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
