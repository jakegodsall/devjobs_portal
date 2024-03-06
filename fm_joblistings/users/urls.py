from django.urls import path
from .views import register_user, register_client, register_company

app_name = "users"
urlpatterns = [
    path("register_user/", register_user, name="register_user"),
    path("register_client/", register_client, name="register_client"),
    path("register_company/", register_company, name="register_company")
]