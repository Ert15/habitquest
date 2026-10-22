from django.test import TestCase

from users.models import User

from .models import Category, Habit


class HabitTests(TestCase):
    def test_habit_str(self) -> None:
        user = User.objects.create_user("bob", "bob@example.com", "pass")
        category = Category.objects.create(name="Sport")
        habit = Habit.objects.create(
            user=user,
            category=category,
            title="Run",
        )
        self.assertEqual(str(habit), "Run (bob)")

    def test_category_can_be_deleted_without_deleting_habit(self) -> None:
        user = User.objects.create_user("bob", "bob@example.com", "pass")
        category = Category.objects.create(name="Sport")
        habit = Habit.objects.create(
            user=user,
            category=category,
            title="Run",
        )
        category.delete()
        habit.refresh_from_db()
        self.assertIsNone(habit.category)
