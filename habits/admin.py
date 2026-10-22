from django.contrib import admin

from .models import Category, Habit


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    search_fields = ("name",)


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "category",
        "frequency",
        "xp_reward",
        "is_active",
        "created_at",
    )
    list_filter = ("frequency", "is_active", "category")
    search_fields = ("title", "user__username")
    list_editable = ("is_active",)
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
    autocomplete_fields = ("user",)

    fieldsets = (
        ("Main info", {"fields": ("user", "title", "description")}),
        ("Settings", {"fields": ("category", "frequency", "xp_reward")}),
        ("Status", {"fields": ("is_active", "created_at")}),
    )
