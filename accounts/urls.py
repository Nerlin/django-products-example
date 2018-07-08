from django.urls import path

from accounts.views import AccountRegistration, AccountRegistrationSuccess, AccountLogin, AccountLogout

app_name = "accounts"
urlpatterns = [
    path("accounts/register/", AccountRegistration.as_view(), name="register"),
    path("accounts/register-success/", AccountRegistrationSuccess.as_view(), name="register-success"),
    path("accounts/login/", AccountLogin.as_view(), name="login"),
    path("accounts/logout/", AccountLogout.as_view(), name="logout")
]
