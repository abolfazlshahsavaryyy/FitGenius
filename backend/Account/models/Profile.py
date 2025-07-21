from django.contrib.auth.models import AbstractUser
from django.db import models
from models.ApplicationUser import ApplicationUser
from django.core.validators import MaxValueValidator, MinValueValidator
class Profile(models.Model):
    user = models.OneToOneField(ApplicationUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
    
class CoachProfile(models.Model):
    years_of_experience=models.IntegerChoices(max=100)
    certifications=models.CharField(max_length=100)
    description=models.CharField(max_length=500)

class NutritionistProfile(models.Model):
    user = models.OneToOneField('Account.ApplicationUser', on_delete=models.CASCADE, related_name='nutritionist_profile')

    certifications = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
    years_of_experience = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class AcademicEducation(models.TextChoices):
        DIPLOMA = 'diploma', 'Diploma'
        BACHELORS = 'bachelors', 'Bachelor’s Degree'
        MASTERS = 'masters', 'Master’s Degree'
        PHD = 'phd', 'PhD'

    academic_education = models.CharField(
        max_length=20,
        choices=AcademicEducation.choices,
        default=AcademicEducation.BACHELORS
    )

    def __str__(self):
        return f"Nutritionist: {self.user.username}"