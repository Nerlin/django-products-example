from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class AccountRegistration(CreateView):
    template_name = "accounts/registration.html"
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy("accounts:register_success")


class AccountRegistrationSuccess(TemplateView):
    template_name = "accounts/registration_success.html"


class AccountLogin(LoginView):
    template_name = "accounts/login.html"


class AccountLogout(LogoutView):
    next_page = reverse_lazy("products:list")
