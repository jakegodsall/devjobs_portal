# routing
from django.shortcuts import render, redirect, get_object_or_404
# scripts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# messages
from django.contrib import messages

from .models import UserProfile, Company, Client
from .forms import UserProfileForm, ClientForm, CompanyForm


def login_user(request):
    context = {"footer_theme": "dark"}
    if request.method == "POST":
        # get the user credentials from the form submission
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if user is authenticated connect user to current session
            login(request, user)
            # create login success message
            messages.success(request, 'You have successfully logged in')
            # redirect to the main jobs page
            return redirect("jobs:index")
        else:
            # create login failure message
            messages.error(request, 'Invalid username or password. Please try again.')
    login_form = AuthenticationForm()
    context["login_form"] = login_form
    return render(request, "users/login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect("jobs:index")


def register_user(request):
    context = {"footer_theme": "dark"}

    user_type = request.GET.get('user_type', None)

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            # Save the user and determine the type
            user = profile_form.save()
            user_type = profile_form.cleaned_data["user_type"]

            # Redirect based on the user type
            if user_type == "client":
                return redirect("users:register_client", user_id=user.pk)
            if user_type == "company":
                return redirect("users:register_company", user_id=user.pk)
        # If the form is invalid, log errors and display the form with errors
        else:
            print(profile_form.errors)
            context["profile_form"] = profile_form
            return render(request, "users/register_user.html", context)

    # If GET request, instantiate the form with or without initial values
    else:
        if user_type:
            profile_form = UserProfileForm(initial={'user_type': user_type})
        else:
            profile_form = UserProfileForm()

    # Always pass the form in context for GET and POST
    context["profile_form"] = profile_form
    return render(request, "users/register_user.html", context)


def register_client(request, user_id):
    context = {"footer_theme": "dark"}
    user = get_object_or_404(UserProfile, pk=user_id)
    if request.method == "POST":
        client_form = ClientForm(request.POST, request.FILES)
        context["client_form"] = client_form
        if client_form.is_valid():
            client_profile = client_form.save(commit=False)
            client_profile.profile = user
            client_profile.save()
            return redirect("users:profile")
        else:
            return render(request, "users/register_client.html", context)
    client_form = ClientForm()
    context["client_form"] = client_form
    return render(request, "users/register_client.html", context)


def register_company(request, user_id):
    context = {"footer_theme": "dark"}
    user = get_object_or_404(UserProfile, pk=user_id)
    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES)
        context["company_form"] = company_form
        if company_form.is_valid():
            company_profile = company_form.save(commit=False)
            company_profile.profile = user
            company_profile.save()
            return redirect("users:profile")
        else:
            print(company_form.errors)
            return render(request, "users/register_company.html", {"company_form": company_form})
    company_form = CompanyForm()
    context["company_form"] = company_form
    return render(request, "users/register_company.html", context)


@login_required
def profile(request):
    context = {
        'footer_theme': 'dark'
    }
    user_profile = request.user
    context['user_profile'] = user_profile
    user_type = user_profile.user_type.lower()
    if user_profile.is_superuser:
        return render(request, "users/superuser_profile.html", context)
    if user_type == "client":
        client_profile = get_object_or_404(Client, profile=user_profile)
        context['client_profile'] = client_profile
        return render(request, "users/client_profile.html", context)
    if user_type == "company":
        company_profile = get_object_or_404(Company, profile=user_profile)
        context['company_profile'] = company_profile
        return render(request, "users/company_profile.html", context)
    return redirect("users:login")
