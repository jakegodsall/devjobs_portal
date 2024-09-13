from django.contrib import admin
from .models import Language, Tool, Job, JobApplication

# Register your models here.
admin.site.register(Language)
admin.site.register(Tool)
admin.site.register(Job)
admin.site.register(JobApplication)