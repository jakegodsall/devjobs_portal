from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    UserProfile extends the base User model to include additional fields that
    are pertinent to all users, regardless of their type. It utilizes a One-to-One
    relationship with the User model to ensure that each user has a unique profile.
    The model distinguishes between different user types, such as clients and companies,
    to cater to the distinct functionalities and permissions each type requires.

    Attributes:
        user (User): A one-to-one link to Django's built-in User model.
        email (EmailField): The user's email address, ensuring uniqueness across the user base.
        user_type (CharField): The type of user, which can be either a Client or a Company, as defined by the Type enum.
    """

    class Type(models.TextChoices):
        CLIENT = "Client", "Client"
        COMPANY = "Company", "Company"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    user_type = models.CharField(max_length=10, choices=Type.choices)

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

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField()
    cv = models.FileField()

class Company(models.Model):
    """
    The Company model caters to users that host job listings, providing them with
    a platform to present their company information and post job opportunities.
    It links back to the UserProfile for authentication and user management, while
    also incorporating company-specific fields for a comprehensive company profile.

    Attributes:
        profile (UserProfile): A one-to-one link to the UserProfile model for common user attributes.
        company_name (CharField): The official name of the company.
        logo (FileField): A digital logo representing the company.
        location (CharField): The physical location or headquarters of the company.
    """

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    logo = models.FileField()
    location = models.CharField(max_length=100)
