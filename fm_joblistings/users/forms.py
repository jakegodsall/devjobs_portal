from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = ["username", "email", "first_name", "last_name"]
#         fields = "__all__"

class UserProfileForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email", "password1", "password2", "user_type"]