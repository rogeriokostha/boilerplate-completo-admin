# 🧱 Boilerplate Completo para Admin – Django + DRF

Boilerplate profissional em **Django Rest Framework** com **autenticação JWT**, **painel administrativo Jazzmin**, **documentação automática (Swagger/Redoc)**, **localização (cidades do Brasil)** e **testes automatizados**.

![Django Tests](https://github.com/rogeriokostha/boilerplate-completo-admin/actions/workflows/tests.yml/badge.svg)

---

## 🚀 Tecnologias Principais

- 🐍 **Django 5+**
- ⚙️ **Django Rest Framework (DRF)**
- 🔐 **JWT (SimpleJWT)**
- 🧭 **Jazzmin Admin**
- 🧩 **drf-spectacular (Swagger / Redoc)**
- 🌐 **CORS Headers**
- 🗄️ **SQLite / PostgreSQL**
- 🧪 **Testes automatizados**
- ⚡ **Busca performática com Trigram (PostgreSQL)**

---

## 🧩 Estrutura do Projeto

```
digitalizador_base/
│
├── core_base/      # Configurações globais e URLs principais
├── accounts/       # Autenticação via e-mail e JWT
├── locations/      # Países, estados, cidades e endereços
├── scripts/        # Scripts utilitários (fixtures, IBGE, etc.)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Instalação Local

```bash
git clone https://github.com/rogeriokostha/boilerplate-completo-admin.git
cd boilerplate-completo-admin

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Rodar migrações e servidor
python manage.py migrate
python manage.py runserver
```
pip install psycopg2-binary

---

## 🧪 Testes Automatizados

```bash
python manage.py test
```

### 🔍 Módulos testados
- **accounts/** → registro, login JWT, redefinição e alteração de senha  
- **locations/** → listagem, paginação e busca acento-insensível  

---

## ☁️ CI/CD (GitHub Actions)

Fluxo automatizado de testes a cada push no branch `main`.

📄 Arquivo do pipeline:  
`.github/workflows/tests.yml`

---

## 📜 Licença

Este projeto é **open source**, sob a licença **MIT**.  
Sinta-se livre para usar, modificar e distribuir.

---

### 🧠 Criado por **Digitalizador de Ideias**

> Inspirando pessoas a transformarem suas ideias em negócios digitais.

---

### Manul de instalação :

📄 README.md — Setup do Projeto Django (Digitalizador Base)
# 🧩 Digitalizador Base — Setup para Novos Projetos (Django + DRF + Postgres + Docker)

Este guia documenta o passo a passo oficial para criar um novo sistema utilizando o **Boilerplate Completo Admin** — Django 5, DRF, JWT, Jazzmin, documentação automática, IBGE completo e PostgreSQL via Docker.

---

# 🚀 1. Criar o diretório do novo projeto

```powershell
mkdir C:\projetos\novo-sistema
cd C:\projetos\novo-sistema

🚀 2. Clonar o boilerplate
git clone https://github.com/rogeriokostha/boilerplate-completo-admin.git

🚀 3. Mover os arquivos para a raiz do projeto

Copie todo o conteúdo interno da pasta:

boilerplate-completo-admin/


E cole diretamente dentro de:

novo-sistema/


Depois apague a pasta boilerplate-completo-admin.

Estrutura final:

novo-sistema/
    accounts/
    core_base/
    locations/
    scripts/
    manage.py
    requirements.txt
    ...

🐘 4. Criar o Docker Compose com PostgreSQL

Crie o arquivo:

📁 docker-compose.yml

Conteúdo:

version: "3.9"

services:
  postgres:
    image: postgres:16
    container_name: digitalizador_postgres
    restart: always
    environment:
      POSTGRES_USER: landinguser
      POSTGRES_PASSWORD: landingpass
      POSTGRES_DB: landingdb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:

🐘 5. Subir o banco de dados
docker compose up -d


Acessar via HeidiSQL:

Host: 127.0.0.1

User: landinguser

Password: landingpass

Port: 5432

Database: landingdb

🧪 6. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

📦 7. Instalar dependências do projeto
pip install -r requirements.txt


Se faltar o driver do Postgres (Windows):

pip install psycopg2-binary

⚙ 8. Configurar o arquivo core_base/settings/local.py

Substituir a configuração de DATABASES por:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "landingdb",
        "USER": "landinguser",
        "PASSWORD": "landingpass",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


Verificar se o manage.py aponta para:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_base.settings.local")

🗃 9. Rodar as migrações
python manage.py migrate

🌍 10. Carregar fixtures do IBGE (países, estados, cidades)
python manage.py loaddata locations/fixtures/countries.json
python manage.py loaddata locations/fixtures/states.json
python manage.py loaddata locations/fixtures/cities.json

👤 11. Criar superusuário
python manage.py createsuperuser

▶ 12. Rodar o servidor
python manage.py runserver


Acessos:

Admin Jazzmin → http://127.0.0.1:8000/admin/

Swagger → http://127.0.0.1:8000/api/docs/

Redoc → http://127.0.0.1:8000/api/redoc/

✅ Pronto!

Você agora tem um ambiente completo:

Django 5 + DRF

JWT

Painel Jazzmin

PostgreSQL em Docker

IBGE completo carregado

Estrutura pronta para novos apps

Documentação automática

Ambiente local isolado

Deploy facilitado
