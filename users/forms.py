from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Client, Company

class UserProfileForm(UserCreationForm):
    CHOICES = [("Client", "Client"), ("Company", "Company")]

    user_type = forms.ChoiceField(label="User Type", choices=CHOICES)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["user_type", "username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username", "class": "form-text-input"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email", "class": "form-text-input"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-text-input"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "<PASSWORD>", "class": "form-text-input"}),
        }



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "avatar", "cv"]



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields =  ["company_name", "logo", "location"]