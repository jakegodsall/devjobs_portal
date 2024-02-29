from django.db import models


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
    is_new = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    languages = models.ManyToManyField(Language, blank=True)
    tools = models.ManyToManyField(Tool, blank=True)

    def __str__(self):
        return f"{self.position} ({self.company})"