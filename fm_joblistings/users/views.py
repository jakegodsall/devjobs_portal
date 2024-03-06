from django.shortcuts import render, redirect
from .forms import UserProfileForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile_form.save()
            return redirect("jobs:index")
        
    profile_form = UserProfileForm()
    return render(request, "users/register.html", {
        "profile_form": profile_form
    })