from django.db import models
from django.utils import timezone

from habits.models import Habit


class CheckIn(models.Model):
    """A mark that the habit was done on some day."""

    class Mood(models.IntegerChoices):
        BAD = 1, "Bad"
        NORMAL = 2, "Normal"
        GOOD = 3, "Good"

    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="checkins",
    )
    date = models.DateField(default=timezone.localdate)
    mood = models.PositiveSmallIntegerField(
        choices=Mood.choices,
        default=Mood.NORMAL,
    )
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        # one habit can be checked only one time per day
        constraints = [
            models.UniqueConstraint(
                fields=["habit", "date"],
                name="unique_checkin_per_day",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.habit.title} - {self.date}"

    def save(self, *args, **kwargs) -> None:
        """Give xp to the user only when the check-in is new."""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.habit.user.add_xp(self.habit.xp_reward)
