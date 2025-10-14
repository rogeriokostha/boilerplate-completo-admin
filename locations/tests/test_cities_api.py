from rest_framework.test import APITestCase
from rest_framework import status
from locations.models import Country, State, City


class CityAPITest(APITestCase):
    def setUp(self):
        # Cria país e estados
        country = Country.objects.create(name="Brasil", code="BR")
        state_sp = State.objects.create(name="São Paulo", uf="SP", country=country)
        state_rj = State.objects.create(name="Rio de Janeiro", uf="RJ", country=country)

        # Cria cidades com e sem acento
        City.objects.create(name="São José do Rio Preto", state=state_sp)
        City.objects.create(name="Sao Joao da Boa Vista", state=state_sp)
        City.objects.create(name="Rio de Janeiro", state=state_rj)

    def test_list_cities_returns_200(self):
        """Verifica se o endpoint de cidades responde com sucesso."""
        response = self.client.get("/api/locations/cities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertGreater(len(response.data["results"]), 0)

    def test_filter_city_by_name_with_accent(self):
        """Busca deve funcionar mesmo com acento (São)."""
        response = self.client.get("/api/locations/cities/?q=sao")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [item["name"].lower() for item in response.data["results"]]
        self.assertTrue(any("são josé" in r or "sao joao" in r for r in results))

    def test_filter_city_partial_word(self):
        """Busca deve retornar resultados parciais (ex: 'rio')."""
        response = self.client.get("/api/locations/cities/?q=rio")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [item["name"].lower() for item in response.data["results"]]
        self.assertTrue(any("rio" in r for r in results))
