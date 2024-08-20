from django.db import models

# Create your models here.
class Pages(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    h1 = models.CharField(max_length=60, null=False)
    
    def __str__(self):
        return self.name
    
class Projects(models.Model):
    project_name = models.CharField(max_length=255, unique=True, null=False)
    client_name = models.CharField(max_length=60, null=False)
    client_description = models.TextField(max_length=255, null=False)
    project_goal = models.TextField(max_length=255)
    experience = models.TextField(max_length=510)
    outcome = models.TextField(max_length=255)
    screenshot = models.URLField()
    project_url = models.URLField()
    
    def __str__(self):
        return self.project_name