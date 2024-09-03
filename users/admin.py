from django.contrib import admin
from .models import UserProfile, Client, Company

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Client)
admin.site.register(Company)
