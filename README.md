<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
  <img src="https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" />
</div>

<div align="center">
  <h1>🧱 Boilerplate Completo para Admin – Django + DRF</h1>
  <p><i>Uma base sólida, escalável e segura para acelerar o desenvolvimento de sistemas e APIs empresariais.</i></p>
</div>

<br/>

Este projeto é um **Boilerplate avançado em Django**, idealizado para poupar horas de configuração inicial. Ele já vem com autenticação JWT, documentação automática de APIs, painel administrativo modernizado, suporte multi-idiomas e ambiente conteinerizado.

---

## 🚀 Tecnologias e Funcionalidades Principais

*   **Django & Django REST Framework (DRF):** Backend robusto e escalável.
*   **Autenticação JWT:** Implementada com `djangorestframework-simplejwt`.
*   **Documentação Automática:** Integração com Swagger/ReDoc via `drf-yasg`.
*   **Painel Administrativo Melhorado:** Utilizando `django-jazzmin` para um visual moderno e customizável.
*   **Localização (i18n):** Pronto para sistemas multilíngues.
*   **Variáveis de Ambiente:** Gerenciadas via `django-environ`.
*   **Docker & Docker Compose:** Ambiente de desenvolvimento encapsulado e pronto para rodar.
*   **Testes Automatizados:** Configuração robusta para testes de Views, Models, Serializers e APIs.
*   **CI/CD Pipeline:** Configuração base para o GitHub Actions.

---

## 🧩 Estrutura do Projeto

*   **`core/`**: Configurações principais do Django (`settings.py`, `urls.py`).
*   **`apps/`**: Diretório modular para seus aplicativos Django (ex: `apps/users/`, `apps/products/`).
*   **`requirements.txt` / `Pipfile`**: Gerenciamento de dependências.
*   **`Dockerfile` e `docker-compose.yml`**: Infraestrutura local em contêineres.

---

## ⚙️ Instalação Local e Setup Inicial

Siga os passos abaixo para rodar o projeto em sua máquina usando Docker:

### 1. Clone o repositório
```bash
git clone https://github.com/rogeriokostha/boilerplate-completo-admin.git
cd boilerplate-completo-admin
```

### 2. Configure as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:
```bash
cp .env.example .env
```
*(Não se esqueça de ajustar as credenciais de banco de dados e a SECRET_KEY).*

### 3. Suba os Contêineres (Docker)
```bash
docker-compose up --build -d
```

### 4. Execute as Migrações e Crie o Superusuário
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

O servidor estará rodando em `http://localhost:8000`.

---

## 🧪 Testes Automatizados

A base já inclui suítes de testes. Para rodar a bateria completa:

```bash
docker-compose exec web python manage.py test
```

### Módulos recomendados para teste:
*   🔑 Autenticação JWT.
*   🛠️ Endpoints do CRUD via DRF.
*   🔐 Permissões de Usuários.

---

## 🧠 Criado por
**Rogerio Costa | Digitalizador de Ideias**
*   **Blog:** [www.digitalizadordeideias.com.br](http://www.digitalizadordeideias.com.br)
*   **LinkedIn:** [rogeriokostha](https://www.linkedin.com/in/rogeriokostha/)

---
<div align="center">
  📜 <b>Licença MIT</b> - Sinta-se livre para clonar, modificar e usar em seus projetos comerciais ou pessoais.
</div>