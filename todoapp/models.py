from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Child(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Childd'
        verbose_name_plural = 'Children'