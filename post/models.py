from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
