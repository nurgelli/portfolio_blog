from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
class Location(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='jobs', null=True)
    location = models.CharField(max_length=256, choices=[
        ('ashgabat', 'Ashgabat'),
        ('mary', 'Mary'),
        ('dashoguz', 'Dashoguz'),
    ], default='Ashgabat', null=False, blank=False)
    
    def __str__(self):
        return f'{self.location} > {self.job.title}'

