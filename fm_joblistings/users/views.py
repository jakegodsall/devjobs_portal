from django.shortcuts import render, redirect
from .forms import UserProfileForm, ClientForm, CompanyForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile_form.save()
            if profile_form.user_type == "client":
                return redirect("users:register_client")
            if profile_form.user_type == "company":
                return redirect("users:register_company")
        
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