from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthAPITest(APITestCase):
    def setUp(self):
        # Usuário de teste padrão
        self.user_data = {
            "email": "teste@example.com",
            "password": "senha123",
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_register_user(self):
        """Deve registrar um novo usuário com sucesso."""
        data = {
            "email": "novo@example.com",
            "password": "teste456",
            "password2": "teste456",
            "first_name": "Novo",
            "last_name": "Usuário",
        }
        response = self.client.post("/api/accounts/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertTrue(User.objects.filter(email="novo@example.com").exists())

    def test_login_with_email_and_password(self):
        """Deve autenticar usuário existente e retornar tokens JWT."""
        response = self.client.post(
            "/api/accounts/token/",
            {"email": self.user_data["email"], "password": self.user_data["password"]},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_with_invalid_credentials(self):
        """Não deve autenticar com senha incorreta."""
        response = self.client.post(
            "/api/accounts/token/",
            {"email": self.user_data["email"], "password": "errada"},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
