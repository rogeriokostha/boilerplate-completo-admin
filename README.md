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
