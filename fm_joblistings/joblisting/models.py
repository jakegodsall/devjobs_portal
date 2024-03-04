from datetime import datetime, timedelta
from django.db import models
from django.utils.timezone import make_aware, get_default_timezone


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='logos/', null=True)
    
    def __str__(self):
        return self.name
    

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    class Role(models.TextChoices):
        FRONTEND = "FE", "Frontend"
        FULLSTACK = "FS", "Fullstack"
        BACKEND = "BE", "Backend"

    class Level(models.TextChoices):
        JUNIOR = "J", "Junior"
        MIDWEIGHT = "M", "Midweight"
        SENIOR = "S", "Senior"
    
    class Contract(models.TextChoices):
        PART_TIME = "PT", "Part Time"
        FULL_TIME = "FT", "Full Time"
    
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=Role.choices)    
    level = models.CharField(max_length=1, choices=Level.choices, default=Level.JUNIOR)
    contract = models.CharField(max_length=2, choices=Contract.choices, default=Contract.FULL_TIME)
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    languages = models.ManyToManyField(Language, blank=True)
    tools = models.ManyToManyField(Tool, blank=True)

    def __str__(self):
        return f"{self.position} ({self.company})"
    
    def is_new(self):
        """
        Returns whether the job was posted within the last week.

        Returns:
            bool: Whether the job was posted within the last week.
        """
        one_week_ago = make_aware(datetime.now(), get_default_timezone()) - timedelta(weeks=1)
        return self.posted_at > one_week_ago
    
    def format_duration(self):
        """
        Returns a human-friendly representation of the duration since the job was posted.

        Returns:
            str: A human-friendly representation of the duration.
        """
        DAYS_IN_MONTH = 30
        DAYS_IN_WEEK = 7

        total_days = (make_aware(datetime.now(), get_default_timezone()) - self.posted_at).days
        months, remainder = divmod(total_days, DAYS_IN_MONTH)
        weeks, days = divmod(remainder, DAYS_IN_WEEK)

        result = { "months": months, "weeks": weeks, "days": days }

        if result.get("months") != 0:
            return f"{result.get('months')}m ago"
        if result.get("weeks") != 0:
            return f"{result.get('weeks')}w ago"
        return f"{result.get('days')}d ago"
