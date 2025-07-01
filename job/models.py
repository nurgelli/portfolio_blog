from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    
class Location(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE),
    location = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.location}'

