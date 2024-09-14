from django.urls import path
from .views import IndexView, CreateJobView, MyApplicationsView

from django.conf import settings
from django.conf.urls.static import static

app_name = "jobs"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('create/', CreateJobView.as_view(), name="create_job"),
    path('my-applications/', MyApplicationsView.as_view(), name="my_applications")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)