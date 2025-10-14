from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer para exibir dados do usuário autenticado"""

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "date_joined"]
        read_only_fields = ["id", "email", "date_joined"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Permite login via e-mail em vez de username"""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["name"] = user.first_name or ""
        return token

    def validate(self, attrs):
        username_field = self.username_field
        attrs[username_field] = attrs.get("email", attrs.get(username_field))
        return super().validate(attrs)


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer para registrar novos usuários"""

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer para alteração de senha do usuário autenticado"""

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        user = self.context["request"].user
        old_password = attrs.get("old_password")

        if not check_password(old_password, user.password):
            raise serializers.ValidationError(
                {"old_password": "Senha atual incorreta."}
            )

        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError(
                {"new_password": "As senhas não coincidem."}
            )

        return attrs

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user


class PasswordResetRequestSerializer(serializers.Serializer):
    """Solicita redefinição de senha por e-mail"""

    email = serializers.EmailField()

    def validate_email(self, value):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Nenhum usuário encontrado com este e-mail."
            )
        return value

    def save(self):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        user = User.objects.get(email=self.validated_data["email"])
        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        reset_link = (
            f"http://127.0.0.1:8000/api/accounts/reset-password-confirm/{uid}/{token}/"
        )

        send_mail(
            subject="Redefinição de senha",
            message=f"Use o link abaixo para redefinir sua senha:\n{reset_link}",
            from_email=None,
            recipient_list=[user.email],
        )
        return {"detail": "E-mail de redefinição enviado."}


class PasswordResetConfirmSerializer(serializers.Serializer):
    """Confirma redefinição de senha"""

    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs

    def save(self):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        try:
            uid = force_str(urlsafe_base64_decode(self.validated_data["uid"]))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError("Link inválido ou expirado.")

        token = self.validated_data["token"]
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("Token inválido ou expirado.")

        user.set_password(self.validated_data["new_password"])
        user.save()
        return {"detail": "Senha redefinida com sucesso."}
