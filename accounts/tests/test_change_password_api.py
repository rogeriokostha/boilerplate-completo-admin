from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class ChangePasswordAPITest(APITestCase):
    def setUp(self):
        # Cria usuário de teste
        self.user = User.objects.create_user(
            email="usuario@example.com", password="senha123"
        )

        # Autentica e obtém token JWT
        login_response = self.client.post(
            "/api/accounts/token/",
            {"email": "usuario@example.com", "password": "senha123"},
        )
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.access_token = login_response.data["access"]

        # Define header de autorização
        self.auth_header = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

    def test_change_password_success(self):
        """Usuário autenticado deve conseguir alterar sua senha."""
        data = {
            "old_password": "senha123",
            "new_password": "novaSenha456",
            "new_password2": "novaSenha456",
        }
        response = self.client.put(
            "/api/accounts/change-password/", data, **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("novaSenha456"))

    def test_change_password_wrong_old_password(self):
        """Deve falhar se a senha antiga estiver incorreta."""
        data = {
            "old_password": "errada",
            "new_password": "novaSenha789",
            "new_password2": "novaSenha789",
        }
        response = self.client.put(
            "/api/accounts/change-password/", data, **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("old_password", response.data)

    def test_change_password_mismatch_new_passwords(self):
        """Deve falhar se as novas senhas não coincidirem."""
        data = {
            "old_password": "senha123",
            "new_password": "novaSenha123",
            "new_password2": "outraSenha",
        }
        response = self.client.put(
            "/api/accounts/change-password/", data, **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("new_password", response.data)
