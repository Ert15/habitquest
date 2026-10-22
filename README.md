# HabitQuest

Habit tracker with gamification. Django midterm project.

A user creates habits, checks them every day, gets XP and levels,
earns badges and competes with friends in challenges.

## Apps (5)

| App            | Models                          | What it does                               |
|----------------|---------------------------------|--------------------------------------------|
| `users`        | `User` (custom, AbstractUser)   | accounts, xp and level                     |
| `habits`       | `Category`, `Habit`             | habits of the user and their categories    |
| `checkins`     | `CheckIn`                       | daily marks, gives xp to the user          |
| `achievements` | `Achievement`, `UserAchievement`| badges and who got them                    |
| `challenges`   | `Challenge`, `Participation`    | competitions between users, score          |

## ER diagram

![ER diagram](docs/er_diagram.png)

The same diagram as text (Mermaid): `docs/er_diagram.mmd`.

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/

## Checks

```bash
flake8 .             # PEP8
python manage.py test
```

## Admin panel

* theme: `django-jazzmin` (3rd party lib)
* `list_display`, `list_filter`, `search_fields`, `date_hierarchy`
* `fieldsets` for users and habits
* `TabularInline` for badges and challenge participants
* `list_editable`, `readonly_fields`, `autocomplete_fields`
* custom columns (`get_user`, `get_participants_count`)
