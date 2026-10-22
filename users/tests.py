from django.test import TestCase

from .models import User


class UserTests(TestCase):
    def test_new_user_starts_with_level_one(self) -> None:
        user = User.objects.create_user("anna", "anna@example.com", "pass")
        self.assertEqual(user.level, 1)
        self.assertEqual(user.xp, 0)

    def test_add_xp_changes_level(self) -> None:
        user = User.objects.create_user("anna", "anna@example.com", "pass")
        user.add_xp(250)
        self.assertEqual(user.xp, 250)
        self.assertEqual(user.level, 3)
