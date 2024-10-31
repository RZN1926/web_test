from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.name
