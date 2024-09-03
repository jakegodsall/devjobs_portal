from django.views import View
from django.shortcuts import render, redirect

from .models import Job
from .forms import JobForm


# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(
        request,
        'job_portal/index.html',
        {"jobs": jobs}
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