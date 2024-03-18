from django.views import View
from django.shortcuts import render, redirect

from .models import Job
from .forms import JobForm


# Create your views here.
def index(request):
    joblistings = Job.objects.all().prefetch_related('languages').prefetch_related('tools')
    print(joblistings.get(pk=1))
    return render(
        request,
        'joblisting/index.html',
        {"joblistings": joblistings}
    )

class CreateJobView(View):
    form_class = JobForm
    template = "joblisting/create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jobs:index")
        return render(request, self.template, {"form": form})