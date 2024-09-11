from django.urls import path
from .views import index, CreateJobView

from django.conf import settings
from django.conf.urls.static import static

app_name = "jobs"
urlpatterns = [
    path('', index, name="index"),
    path('create', CreateJobView.as_view(), name="create_job")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)