from django.contrib.auth.models import AbstractUser
from django.db import models
from models.ApplicationUser import ApplicationUser
class Profile(models.Model):
    user = models.OneToOneField(ApplicationUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
