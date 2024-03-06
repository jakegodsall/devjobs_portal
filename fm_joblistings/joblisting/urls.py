from django.urls import path
from .views import index, create_job

app_name = "jobs"
urlpatterns = [
    path('', index, name="index"),
    path('create/', create_job, name="create_job")
]