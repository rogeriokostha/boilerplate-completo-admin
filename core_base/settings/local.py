from .base import *
from decouple import config

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# CORS liberado para dev
CORS_ALLOW_ALL_ORIGINS = True

# Banco de dados local (lendo do .env)
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
    }
}

# E-mails exibidos no terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "Digitalizador <no-reply@digitalizador.com>"

# 📦 DRF - Configurações adicionais (pode expandir depois)
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]
