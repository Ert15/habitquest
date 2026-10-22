# Notes for the defense

Read this before the defense. Try to explain every point with your own words.

## 1. Project structure

* `config/` - project settings (`settings.py`, `urls.py`)
* `users/`, `habits/`, `checkins/`, `achievements/`, `challenges/` - apps
* every app has `models.py` (tables) and `admin.py` (admin panel)

## 2. Custom user

```python
class User(AbstractUser):
    email = models.EmailField(unique=True)
    ...
```

* `AbstractUser` is the standard Django user with username, password,
  first_name and so on. We inherit from it and add our fields: `bio`,
  `xp`, `level`.
* In `settings.py` we wrote `AUTH_USER_MODEL = "users.User"`. Because of it
  Django uses our model everywhere.
* We must do it **before the first migration**. Changing it later is painful.
* In other models we do not import `User` directly. We write
  `settings.AUTH_USER_MODEL`.

## 3. Relations between models

| Relation        | Where                                   | Type          |
|-----------------|-----------------------------------------|---------------|
| User - Habit    | `Habit.user`                            | ForeignKey    |
| Category - Habit| `Habit.category` (`SET_NULL`)           | ForeignKey    |
| Habit - CheckIn | `CheckIn.habit`                         | ForeignKey    |
| User - Achievement | `UserAchievement`                    | many-to-many through a table |
| User - Challenge | `Participation`                        | many-to-many through a table |

* `on_delete=CASCADE` - delete the user, his habits are deleted too.
* `on_delete=SET_NULL` - delete the category, the habit stays, category
  becomes empty.
* `related_name` - the name for reverse access: `user.habits.all()`.
* `through="Participation"` - we use our own middle table because it has
  extra fields (`score`, `joined_at`).

## 4. Game logic

* `CheckIn.save()` gives xp to the user, but only when the check-in is new
  (`is_new = self.pk is None`).
* `User.add_xp()` adds xp and counts the level: every 100 xp is a new level.
* `UniqueConstraint(habit, date)` - one habit cannot be checked twice a day.

## 5. Admin panel

* `@admin.register(Model)` - the same as `admin.site.register`.
* `list_display` - columns in the list, `list_filter` - filters on the right,
  `search_fields` - search box.
* `fieldsets` - groups of fields in the edit form.
* `inlines` - edit related objects on the same page.
* `jazzmin` is at the top of `INSTALLED_APPS`, it changes the look of admin.

## 6. Questions the teacher can ask

1. What is the difference between `AbstractUser` and `AbstractBaseUser`?
2. Why do we set `AUTH_USER_MODEL` before the first migration?
3. What is the difference between `CASCADE`, `SET_NULL` and `PROTECT`?
4. What does `related_name` do?
5. Why do we need `through` in `ManyToManyField`?
6. What does `makemigrations` do and what does `migrate` do?
7. What is `Meta` class in the model?
8. Why is `UniqueConstraint` used in `CheckIn`?
9. How does the xp get to the user after a check-in?
10. What is PEP8? How did you check it? (`flake8`)
11. Why do we use type annotations (`-> str`)?
12. Show where in admin you configured filters and search.
13. What is an ER diagram? Show relations on yours.

## 7. Try before the defense

```bash
python manage.py shell
```

```python
from users.models import User
u = User.objects.first()
u.habits.all()          # reverse access by related_name
u.add_xp(50)
```

Also create several habits and check-ins in admin and see how the xp changes.
