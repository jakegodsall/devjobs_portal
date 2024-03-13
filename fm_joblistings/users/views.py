from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserProfileForm, ClientForm, CompanyForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users:profile")
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})
        

# Create your views here.
def register_user(request):
    if request.method == "POST":

        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile_form.save()

            user_type = profile_form.cleaned_data["user_type"].lower()
            print("User type: ", user_type)
            if user_type == "client":
                return redirect("users:register_client")
            if user_type == "company":
                return redirect("users:register_company")
        else:
            print(profile_form.initial)
            print(profile_form.errors)
            return render(request, "users/register_user.html", {"profile_form": profile_form})
        
    profile_form = UserProfileForm()
    return render(request, "users/register_user.html", {
        "profile_form": profile_form
    })


def register_company(request):
    if request.method == "POST":
        ...
    company_form = CompanyForm()
    return render(request, "users/register_company.html", { "company_form": company_form})

def register_client(request):
    if request.method == "POST":
        ...
    client_form = ClientForm()
    return render(request, "users/register_client.html", { "client_form":  client_form})

def profile(request):
    return "Hello"