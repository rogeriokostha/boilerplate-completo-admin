from django.urls import path
from .views import (
    ProfileView,
    CustomTokenObtainPairView,
    RegisterView,
    ChangePasswordView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="user_profile"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", RegisterView.as_view(), name="user_register"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path(
        "reset-password/",
        PasswordResetRequestView.as_view(),
        name="password_reset_request",
    ),
    path(
        "reset-password-confirm/<str:uid>/<str:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
