from django.conf import settings
from django.db import models


class Challenge(models.Model):
    """A competition between friends for some period of time."""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_challenges",
    )
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Participation",
        related_name="challenges",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self) -> str:
        return self.title


class Participation(models.Model):
    """Connection: user takes part in a challenge and has some score."""

    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        related_name="participations",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="participations",
    )
    score = models.PositiveIntegerField(default=0)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score"]
        constraints = [
            models.UniqueConstraint(
                fields=["challenge", "user"],
                name="unique_participation",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.user} in {self.challenge}"
