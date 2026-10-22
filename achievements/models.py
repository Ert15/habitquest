from django.conf import settings
from django.db import models


class Achievement(models.Model):
    """A badge that a user can get."""

    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)
    required_checkins = models.PositiveIntegerField(
        help_text="How many check-ins the user needs to get this badge",
        default=1,
    )
    bonus_xp = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["required_checkins"]

    def __str__(self) -> str:
        return self.name


class UserAchievement(models.Model):
    """Connection: which user got which badge and when."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_achievements",
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name="user_achievements",
    )
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-earned_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "achievement"],
                name="unique_user_achievement",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.user} - {self.achievement}"
