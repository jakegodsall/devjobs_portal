from django.views import View
from django.shortcuts import render, redirect

from .models import Job
from .forms import JobForm


# Create your views here.
def index(request):
    # Get 5 random featured jobs
    featured_jobs = Job.objects.filter(is_featured=True).order_by('?')[:8]

    return render(
        request,
        'job_portal/index.html',
        {"featured_jobs": featured_jobs}
    )

class CreateJobView(View):
    form_class = JobForm
    template = "job_portal/create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jobs:index")
        return render(request, self.template, {"form": form})