from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "level",
        "xp",
        "is_staff",
        "date_joined",
    )
    list_filter = ("is_staff", "is_active", "level")
    search_fields = ("username", "email")
    ordering = ("-xp",)

    # add our own fields to the standard user form
    fieldsets = UserAdmin.fieldsets + (
        ("HabitQuest", {"fields": ("bio", "xp", "level")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("HabitQuest", {"fields": ("email", "bio")}),
    )
