from django.urls import path
from .views import index, CreateJobView

app_name = "jobs"
urlpatterns = [
    path('', index, name="index"),
    path('create', CreateJobView.as_view(), name="create_job")
]