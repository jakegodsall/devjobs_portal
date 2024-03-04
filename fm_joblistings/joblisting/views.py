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

def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")

    form = JobForm()
    return render(request, "joblisting/create.html", {"form": form})