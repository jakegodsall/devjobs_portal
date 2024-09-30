from django import forms
from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User


class UserProfile(auth_models.AbstractUser):
    class Type(models.TextChoices):
        CLIENT = "client", "Client"
        COMPANY = "company", "Company"
        
    user_type = models.CharField(max_length=10, choices=Type.choices)

    USERNAME_FIELD = "username"


class Client(models.Model):
    """
    The Client model is specifically designed for users focused on applying to jobs.
    It extends the UserProfile with client-specific attributes for a more personalized experience.
    This model provides a detailed profile for job seekers, including personal information, an avatar,
    and a resume (CV) for job applications.

    Attributes:
        profile (UserProfile): Associates this client with common user attributes through a one-to-one link.
        first_name (CharField): The first name of the client.
        last_name (CharField): The last name of the client.
        avatar (ImageField): A personal image of the client, used for profile personalization.
        cv (FileField): The client's curriculum vitae, enabling job applications.
    """

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    cv = models.FileField(upload_to='users/cvs/')

    # socials
    portfolio_url = models.URLField(max_length=120, null=True, blank=True)
    github_url = models.URLField(max_length=120, null=True, blank=True)
    linkedin_url = models.URLField(max_length=120, null=True, blank=True)
    twitter_url = models.URLField(max_length=120, null=True, blank=True)
    instagram_url = models.URLField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    """
    The Company model caters to users that host job listings, providing them with
    a platform to present their company information and post job opportunities.
    It links back to the UserProfile for scripts and user management, while
    also incorporating company-specific fields for a comprehensive company profile.

    Attributes:
        profile (UserProfile): A one-to-one link to the UserProfile model for common user attributes.
        company_name (CharField): The official name of the company.
        logo (FileField): A digital logo representing the company.
        location (CharField): The physical location or headquarters of the company.
    """

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True)
    company_name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='users/svg_icons/companies/', blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "companies"
