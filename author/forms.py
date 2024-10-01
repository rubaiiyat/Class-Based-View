from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class editProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
