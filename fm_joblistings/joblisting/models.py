from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Level(models.Model):
    LEVELS = {
        "J": "JUNIOR",
        "M": "MIDWEIGHT",
        "S": "SENIOR"
    }

    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        default="MIDWEIGHT")
    
    def __str__(self):
        return self.LEVELS[self.level]
    

class Contract(models.Model):
    CONTRACT_TYPES = {
        "PT": "Part Time",
        "FT": "Full Time"
    }

    contract = models.CharField(
        max_length=2,
        choices=CONTRACT_TYPES,
        default="FT")
    
    def __str__(self):
        return self.CONTRACT_TYPES[self.contract]
    
    
class Role(models.Model):
    ROLES = {
        "FE": "Frontend",
        "FS": "Fullstack",
        "BE": "Backend"
    }

    role = models.CharField(
        max_length=2,
        choices=ROLES,
        default="FS")
    
    def __str__(self):
        return self.ROLES[self.role]
    
    
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    contract = models.CharField(Contract, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    languages = models.ManyToManyField(Language)
    tools = models.ManyToManyField(Tool)

    def __str__(self):
        return f"self.position (self.company)"