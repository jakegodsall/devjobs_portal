from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Client, Company

class UserProfileForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email", "password1", "password2", "user_type"]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "avatar", "cv"]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields =  ["company_name", "logo", "location"]