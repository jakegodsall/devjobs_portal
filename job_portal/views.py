from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Job, JobApplication
from .forms import JobForm

from users.models import Client


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
        client = get_object_or_404(Client, profile=request.user)
        applications = JobApplication.objects.filter(client=client)

        context = {

            'user': request.user,
            'applications': applications,
            'footer_theme': 'dark'
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