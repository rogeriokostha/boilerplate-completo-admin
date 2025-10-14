from django.db import migrations, connection


def create_trigram_indexes(apps, schema_editor):
    # Evita rodar em SQLite
    if connection.vendor != "postgresql":
        print("🔹 Ignorando criação de índices GIN (não é PostgreSQL).")
        return

    with connection.cursor() as cursor:
        # Habilita extensões
        cursor.execute("CREATE EXTENSION IF NOT EXISTS unaccent;")
        cursor.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

        # Cria índices GIN para buscas trigram
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_city_name_trgm
            ON locations_city USING gin (name gin_trgm_ops);
        """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_state_name_trgm
            ON locations_state USING gin (name gin_trgm_ops);
        """
        )

        print("✅ Índices trigram criados com sucesso.")


def drop_trigram_indexes(apps, schema_editor):
    if connection.vendor != "postgresql":
        return

    with connection.cursor() as cursor:
        cursor.execute("DROP INDEX IF EXISTS idx_city_name_trgm;")
        cursor.execute("DROP INDEX IF EXISTS idx_state_name_trgm;")
        print("🧹 Índices trigram removidos.")


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_trigram_indexes, reverse_code=drop_trigram_indexes),
    ]
