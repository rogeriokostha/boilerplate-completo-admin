from rest_framework.test import APITestCase
from rest_framework import status
from locations.models import Country, State


class StateAPITest(APITestCase):
    def setUp(self):
        # Cria o país e alguns estados para teste
        self.country = Country.objects.create(name="Brasil", code="BR")
        State.objects.create(name="São Paulo", uf="SP", country=self.country)
        State.objects.create(name="Rio de Janeiro", uf="RJ", country=self.country)

    def test_list_states_returns_200(self):
        """Verifica se o endpoint de estados responde com sucesso."""
        response = self.client.get("/api/locations/states/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertGreater(len(response.data["results"]), 0)

    def test_filter_state_by_name(self):
        """Verifica se o filtro ?q= funciona para nomes de estados."""
        response = self.client.get("/api/locations/states/?q=paulo")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [item["name"].lower() for item in response.data["results"]]
        self.assertIn("são paulo", results)

    def test_filter_state_by_uf(self):
        """Verifica se o filtro ?q= funciona com UF."""
        response = self.client.get("/api/locations/states/?q=rj")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [item["uf"].lower() for item in response.data["results"]]
        self.assertIn("rj", results)
