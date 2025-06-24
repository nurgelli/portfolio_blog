from django.db import models

# Create your models here.


class Tech(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
