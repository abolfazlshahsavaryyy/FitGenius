from django.db import models
from django.conf import settings

class NutritionPlan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='nutrition_plans'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Day(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY = 'MON', 'Monday'
        TUESDAY = 'TUE', 'Tuesday'
        WEDNESDAY = 'WED', 'Wednesday'
        THURSDAY = 'THU', 'Thursday'
        FRIDAY = 'FRI', 'Friday'
        SATURDAY = 'SAT', 'Saturday'
        SUNDAY = 'SUN', 'Sunday'

    nutrition_plan = models.ForeignKey(
        NutritionPlan,
        on_delete=models.CASCADE,
        related_name='days'
    )
    name = models.CharField(max_length=100)
    day_of_week = models.CharField(
        max_length=3,
        choices=DayOfWeek.choices
    )

    class Meta:
        unique_together = ('nutrition_plan', 'day_of_week')  # Ensure unique day_of_week per plan

    def __str__(self):
        return f"{self.get_day_of_week_display()} - {self.name}"


class NutritionPlanItem(models.Model):
    class ServingTime(models.TextChoices):
        MORNING = 'MORNING', 'Morning'
        NOON = 'NOON', 'Noon'
        EVENING = 'EVENING', 'Evening'
        NIGHT = 'NIGHT', 'Night'
        SNACK = 'SNACK', 'Snack'
        PRE_WORKOUT = 'PRE', 'Pre-Workout'
        POST_WORKOUT = 'POST', 'Post-Workout'

    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        related_name='items'
    )
    food_name = models.CharField(max_length=100)
    serving_time = models.CharField(
        max_length=12,
        choices=ServingTime.choices
    )
    amount_grams = models.FloatField(help_text="Amount in grams")

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.food_name} ({self.serving_time}) - {self.amount_grams}g"
