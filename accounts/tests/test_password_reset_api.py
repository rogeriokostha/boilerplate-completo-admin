from rest_framework.test import APITestCase
from rest_framework import status
from django.core import mail
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

User = get_user_model()


class PasswordResetAPITest(APITestCase):
    def setUp(self):
        # Cria usuário de teste
        self.user = User.objects.create_user(
            email="usuario@example.com", password="senha123"
        )

    def test_request_password_reset_sends_email(self):
        """Deve enviar e-mail de redefinição de senha."""
        response = self.client.post(
            "/api/accounts/reset-password/", {"email": "usuario@example.com"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Redefinição de senha", mail.outbox[0].subject)
        self.assertIn(
            "http://127.0.0.1:8000/api/accounts/reset-password-confirm/",
            mail.outbox[0].body,
        )

    def test_request_password_reset_invalid_email(self):
        """Não deve enviar e-mail para e-mail inexistente."""
        response = self.client.post(
            "/api/accounts/reset-password/", {"email": "naoexiste@example.com"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_confirm_password_reset_with_valid_token(self):
        """Deve redefinir senha com token válido."""
        token = PasswordResetTokenGenerator().make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = f"/api/accounts/reset-password-confirm/{uid}/{token}/"
        data = {"new_password": "novaSenha123", "new_password2": "novaSenha123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("novaSenha123"))
