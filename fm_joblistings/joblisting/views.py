from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    joblistings = Job.objects.all().prefetch_related('languages').prefetch_related('tools')
    print(joblistings.get(pk=1))
    return render(
        request,
        'joblisting/index.html',
        {"joblistings": joblistings}
    )