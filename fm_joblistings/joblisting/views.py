from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    joblistings = Job.objects.all()
    return render(
        request,
        'joblisting/index.html',
        {"joblistings": joblistings}
    )