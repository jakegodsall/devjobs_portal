from django.shortcuts import render
from .forms import UserProfileForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        ...
    # user_form = UserForm(prefix="user")
    profile_form = UserProfileForm(prefix="profile")
    return render(request, "users/register.html", {
        # "user_form": user_form,
        "profile_form": profile_form
    })