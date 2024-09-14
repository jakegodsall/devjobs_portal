from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect

from .models import Job
from .forms import JobForm


class IndexView(View):
    template = 'job_portal/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # Get 5 random featured jobs
        featured_jobs = Job.objects.filter(is_featured=True).order_by('?')[:8]
        context["featured_jobs"] = featured_jobs

        if request.user.is_authenticated:
            context["user_type"] = request.user.user_type

        return render(
            request,
            'job_portal/index.html',
            context
        )


class MyApplicationsView(LoginRequiredMixin, View):
    template = "job_portal/my-applications.html"

    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user
        }

        return render(request, self.template, context)


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