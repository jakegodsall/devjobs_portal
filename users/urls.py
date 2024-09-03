from django.urls import path
from .views import login_user, logout_user, register_user, register_client, register_company, profile

app_name = "users"
urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register_user/", register_user, name="register_user"),
    path("register_client/<int:user_id>", register_client, name="register_client"),
    path("register_company/<int:user_id>", register_company, name="register_company"),
    path("profile/", profile, name="profile")
]