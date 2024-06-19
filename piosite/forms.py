from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        domain = email.split('@')[-1]
        if domain != "edu.p.lodz.pl":
            raise ValidationError("Rejestracja jest możliwa tylko przy użyciu adresu e-mail @edu.p.lodz.pl")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
