# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class ApplicationUser(AbstractUser):
    # Add domain-specific fields here if needed (e.g., role, phone)
    class Roles(models.TextChoices):
        NORMAL_USER = 'normal_user', 'Normal User'
        COACH = 'coach', 'Coach'
        NUTRITIONIST = 'nutritionist', 'Nutritionist'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.NORMAL_USER
    )

    def is_coach(self):
        return self.role == self.Roles.COACH

    def is_nutritionist(self):
        return self.role == self.Roles.NUTRITIONIST

    def is_normal_user(self):
        return self.role == self.Roles.NORMAL_USER