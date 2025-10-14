from django.db.models import Q
import unicodedata
from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Country, State, City, Address
from .serializers import (
    CountrySerializer,
    StateSerializer,
    CitySerializer,
    AddressSerializer,
)
from .pagination import DefaultPagination
from django.conf import settings
from django.db import connection
from django.db.models import Q


# ------------------------------------------------------------
# 🔹 COUNTRY LIST VIEW
# ------------------------------------------------------------
@extend_schema(
    parameters=[
        OpenApiParameter(
            name="q",
            description="Filtro por nome ou código do país (case-insensitive)",
            required=False,
            type=str,
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="page", description="Número da página", required=False, type=int
        ),
        OpenApiParameter(
            name="page_size",
            description="Itens por página (máx. 100)",
            required=False,
            type=int,
        ),
    ]
)
class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer
    pagination_class = DefaultPagination
    permission_classes = []  # público

    def get_queryset(self):
        qs = Country.objects.all().order_by("name")
        q = self.request.query_params.get("q")
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
        return qs


# ------------------------------------------------------------
# 🔹 STATE LIST VIEW
# ------------------------------------------------------------
@extend_schema(
    parameters=[
        OpenApiParameter(
            name="q",
            description="Filtro por nome, UF ou país (case-insensitive)",
            required=False,
            type=str,
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="page", description="Número da página", required=False, type=int
        ),
        OpenApiParameter(
            name="page_size",
            description="Itens por página (máx. 100)",
            required=False,
            type=int,
        ),
    ]
)
class StateListView(generics.ListAPIView):
    serializer_class = StateSerializer
    pagination_class = DefaultPagination
    permission_classes = []  # público

    def get_queryset(self):
        qs = State.objects.select_related("country").order_by("name")
        q = self.request.query_params.get("q")
        if q:
            qs = qs.filter(
                Q(name__icontains=q)
                | Q(country__name__icontains=q)
                | Q(uf__icontains=q)  # se o modelo tiver campo 'uf'
            )
        return qs


# ------------------------------------------------------------
# 🔹 Funções utilitárias (para busca acento-insensível)
# ------------------------------------------------------------
def normalize_text(text):
    """Remove acentos e converte para minúsculas"""
    if not text:
        return ""
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    ).lower()


# ------------------------------------------------------------
# 🔹 CITY LIST VIEW
# ------------------------------------------------------------
@extend_schema(
    parameters=[
        OpenApiParameter(
            name="q",
            description="Busca performática por nome de cidade, estado ou UF (acento-insensível, com similaridade em Postgres)",
            required=False,
            type=str,
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="page", description="Número da página", required=False, type=int
        ),
        OpenApiParameter(
            name="page_size",
            description="Itens por página (máx. 100)",
            required=False,
            type=int,
        ),
    ]
)
class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    pagination_class = DefaultPagination
    permission_classes = []  # pública

    def get_queryset(self):
        q = self.request.query_params.get("q")
        qs = City.objects.select_related("state").order_by("name")

        if not q:
            return qs

        # Função auxiliar inline (remove acentos da string)
        import unicodedata

        def normalize(text):
            return "".join(
                c
                for c in unicodedata.normalize("NFD", text)
                if unicodedata.category(c) != "Mn"
            ).lower()

        normalized_q = normalize(q)

        # --- Caso SQLite (dev) ---
        if connection.vendor == "sqlite":
            return [
                city
                for city in qs
                if normalized_q in normalize(city.name)
                or normalized_q in normalize(city.state.name)
                or normalized_q in normalize(city.state.uf)
            ]

        # --- Caso PostgreSQL ---
        from django.contrib.postgres.search import TrigramSimilarity
        from django.db.models.functions import Unaccent, Lower

        # Busca acento-insensível em city + state
        qs = qs.annotate(
            sim_city=TrigramSimilarity(Unaccent(Lower("name")), Unaccent(Lower(q))),
            sim_state=TrigramSimilarity(
                Unaccent(Lower("state__name")), Unaccent(Lower(q))
            ),
        ).filter(Q(sim_city__gt=0.05) | Q(sim_state__gt=0.05))

        return qs.order_by("-sim_city", "-sim_state", "name")


# ------------------------------------------------------------
# 🔹 ADDRESS CREATE VIEW
# ------------------------------------------------------------
class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
