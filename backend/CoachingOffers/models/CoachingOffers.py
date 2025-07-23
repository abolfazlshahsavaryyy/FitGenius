from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
class CoachingOffer(models.Model):
    coach = models.ForeignKey(
        'Account.CoachProfile',
        on_delete=models.CASCADE,
        related_name='offers'
    )
    training_program = models.OneToOneField(
        'TrainingProgram.TrainingProgram',  # <== Correct string reference
        on_delete=models.CASCADE,
        related_name='coaching_offer'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    number_of_days = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of days in the coaching plan"
    )

    number_of_exercises = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Total number of exercises included"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Price of the offer in currency units"
    )

    max_capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Maximum number of clients for this offer"
    )
    purchased_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='purchased_offers',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Coach: {self.coach.user.username})"
