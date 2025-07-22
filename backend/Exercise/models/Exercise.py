from django.db import models
from django.conf import settings
class Exercise(models.Model):
    days = models.ManyToManyField(  # Renamed to `days` (plural) for clarity
        'TrainingProgram.Day',
        related_name='exercises',
        blank=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    reps = models.PositiveIntegerField(help_text="Number of sets (e.g., 3)")
    times = models.PositiveIntegerField(help_text="Number of repetitions per set (e.g., 12)")

    rest_seconds = models.PositiveIntegerField(default=60, help_text="Rest between sets in seconds")
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_exercises',
        blank=True
    )
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} (Day: {self.day.get_day_of_week_display()})"


class LinkVideo(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='link_videos'
    )
    url = models.URLField()
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Video for {self.exercise.name}: {self.url}"
