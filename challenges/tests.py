from datetime import date

from django.test import TestCase

from users.models import User

from .models import Challenge, Participation


class ChallengeTests(TestCase):
    def test_user_can_join_challenge(self) -> None:
        creator = User.objects.create_user("lena", "lena@example.com", "p")
        friend = User.objects.create_user("ivan", "ivan@example.com", "p")
        challenge = Challenge.objects.create(
            title="30 days of sport",
            creator=creator,
            start_date=date(2026, 1, 1),
            end_date=date(2026, 1, 30),
        )
        Participation.objects.create(challenge=challenge, user=friend)
        self.assertEqual(challenge.participants.count(), 1)
        self.assertIn(friend, challenge.participants.all())
