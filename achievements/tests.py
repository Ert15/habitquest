from django.db import IntegrityError, transaction
from django.test import TestCase

from users.models import User

from .models import Achievement, UserAchievement


class AchievementTests(TestCase):
    def test_user_cannot_get_same_badge_twice(self) -> None:
        user = User.objects.create_user("max", "max@example.com", "pass")
        badge = Achievement.objects.create(name="First step")
        UserAchievement.objects.create(user=user, achievement=badge)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                UserAchievement.objects.create(user=user, achievement=badge)
