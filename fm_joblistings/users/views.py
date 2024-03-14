from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProfile
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
            user = profile_form.save()

            user_type = profile_form.cleaned_data["user_type"].lower()
            print("User type: ", user_type)
            if user_type == "client":
                return redirect("users:register_client", user_id=user.pk)
            if user_type == "company":
                return redirect("users:register_company", user_id=user.pk)
        else:
            print(profile_form.initial)
            print(profile_form.errors)
            return render(request, "users/register_user.html", {"profile_form": profile_form})
        
    profile_form = UserProfileForm()
    return render(request, "users/register_user.html", {
        "profile_form": profile_form
    })


def register_company(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    print("user_id: ", user_id)
    print(user)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        print("working so far")
        print(form.data)
        if form.is_valid():
            company_profile = form.save(commit=False)
            company_profile.profile = user
            company_profile.save()
            return redirect("users:profile")
        else:
            print(form.errors)
    company_form = CompanyForm()
    return render(request, "users/register_company.html", { "company_form": company_form})

def register_client(request):
    if request.method == "POST":
        ...
    client_form = ClientForm()
    return render(request, "users/register_client.html", { "client_form":  client_form})

def profile(request):
    return "Hello"