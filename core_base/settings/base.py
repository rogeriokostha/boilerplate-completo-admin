from pathlib import Path
import os
from decouple import config, Csv


# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ⚙️ Configurações básicas
SECRET_KEY = config("SECRET_KEY")

# Cada ambiente define o DEBUG e ALLOWED_HOSTS
# no arquivo local.py ou production.py

# 🌎 Idioma e fuso horário
LANGUAGE_CODE = "pt-br"
TIME_ZONE = config("TIME_ZONE", default="America/Sao_Paulo")
USE_I18N = True
USE_TZ = True

# 🧱 Aplicativos principais
INSTALLED_APPS = [
    "jazzmin",  # Tema customizado para o admin
    # Django apps padrões
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    # Django REST Framework
    "rest_framework",
    "drf_spectacular",
    # App principal
    "core",
    # Outros apps podem ser adicionados aqui
    "accounts",
    "locations",
]

# ⚙️ Middlewares padrão
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTH_USER_MODEL = "accounts.User"


# 🔗 URLs e WSGI
ROOT_URLCONF = "core_base.urls"
WSGI_APPLICATION = "core_base.wsgi.application"

# 🎨 Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


CORS_ALLOW_ALL_ORIGINS = True  # modo desenvolvimento (libera tudo)
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOWED_ORIGINS = [
#   "https://seudominio.com",
#   "https://app.seudominio.com",
# ]

# 📂 Arquivos estáticos
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# 📥 Arquivos de mídia (opcional para futuras plataformas)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# 🧩 Configurações padrão de DRF (podemos ajustar depois)
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)  # cria a pasta logs se não existir

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {name}: {message}",
            "style": "{",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "django.log",
            "formatter": "verbose",
        },
        "errors": {
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "errors.log",
            "formatter": "verbose",
            "level": "WARNING",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file", "errors"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["errors"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}


SPECTACULAR_SETTINGS = {
    "TITLE": "API Base - Digitalizador",
    "DESCRIPTION": "Documentação automática da API base com autenticação JWT.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # 🔒 Configuração do botão "Authorize"
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,  # mantém o token salvo
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "SECURITY": [{"BearerAuth": []}],
    "COMPONENTS": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                "description": "Cole aqui seu token JWT no formato: **Bearer <token>**",
            },
        },
    },
}


EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="no-reply@example.com")
