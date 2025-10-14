from rest_framework.test import APITestCase
from rest_framework import status
from locations.models import Country


class CountryAPITest(APITestCase):
    def setUp(self):
        # Cria um país para testar
        Country.objects.create(name="Brasil", code="BR")

    def test_list_countries_returns_200(self):
        """Verifica se o endpoint de países responde com sucesso."""
        response = self.client.get("/api/locations/countries/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertGreater(len(response.data["results"]), 0)

    def test_filter_country_by_query(self):
        """Verifica se o filtro ?q= funciona corretamente."""
        response = self.client.get("/api/locations/countries/?q=bra")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [item["name"].lower() for item in response.data["results"]]
        self.assertIn("brasil", results)
