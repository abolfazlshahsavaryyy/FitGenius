from django.db import models
from django.conf import settings

class TrainingProgram(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='training_programs'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Day(models.Model):
    class WeekDay(models.TextChoices):
        MONDAY = 'monday', 'Monday'
        TUESDAY = 'tuesday', 'Tuesday'
        WEDNESDAY = 'wednesday', 'Wednesday'
        THURSDAY = 'thursday', 'Thursday'
        FRIDAY = 'friday', 'Friday'
        SATURDAY = 'saturday', 'Saturday'
        SUNDAY = 'sunday', 'Sunday'

    training_program = models.ForeignKey(
        TrainingProgram,
        on_delete=models.CASCADE,
        related_name='days'
    )
    day_of_week = models.CharField(
        max_length=10,
        choices=WeekDay.choices
    )

    # Optional extra properties for each day
    notes = models.TextField(blank=True)

    class Meta:
        # Unique constraint: each TrainingProgram can only have one of each day
        unique_together = ('training_program', 'day_of_week')

    def __str__(self):
        return f"{self.training_program.name} - {self.get_day_of_week_display()}"
