from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Our own user model. It is based on the standard Django user."""

    email = models.EmailField("email address", unique=True)
    bio = models.TextField("about me", blank=True)
    xp = models.PositiveIntegerField("experience points", default=0)
    level = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.username

    def add_xp(self, amount: int) -> None:
        """Give the user some xp and recalculate the level.

        Every 100 xp is one new level.
        """
        self.xp += amount
        self.level = self.xp // 100 + 1
        self.save(update_fields=["xp", "level"])
