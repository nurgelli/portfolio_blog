from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name
