from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=64)
    about = models.TextField(default='null')
    image = models.ImageField(default='null')
    technologies = models.CharField()
    
    def __str__(self):
        return self.name
