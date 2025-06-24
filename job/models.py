from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    due_date = models.DateField(blank=True)
    
    def __str__(self):
        return self.name
