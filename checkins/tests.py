from datetime import date

from django.db import IntegrityError, transaction
from django.test import TestCase

from habits.models import Habit
from users.models import User

from .models import CheckIn


class CheckInTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user("kate", "kate@example.com", "p")
        self.habit = Habit.objects.create(
            user=self.user,
            title="Read",
            xp_reward=30,
        )

    def test_checkin_gives_xp(self) -> None:
        CheckIn.objects.create(habit=self.habit, date=date(2026, 1, 1))
        self.user.refresh_from_db()
        self.assertEqual(self.user.xp, 30)

    def test_xp_is_given_only_once(self) -> None:
        checkin = CheckIn.objects.create(
            habit=self.habit,
            date=date(2026, 1, 1),
        )
        checkin.note = "changed"
        checkin.save()
        self.user.refresh_from_db()
        self.assertEqual(self.user.xp, 30)

    def test_two_checkins_on_same_day_are_not_allowed(self) -> None:
        CheckIn.objects.create(habit=self.habit, date=date(2026, 1, 1))
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                CheckIn.objects.create(
                    habit=self.habit,
                    date=date(2026, 1, 1),
                )
