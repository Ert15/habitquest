from django.contrib import admin

from .models import CheckIn


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ("habit", "get_user", "date", "mood", "created_at")
    list_filter = ("mood", "date")
    search_fields = ("habit__title", "habit__user__username", "note")
    date_hierarchy = "date"
    readonly_fields = ("created_at",)
    list_select_related = ("habit", "habit__user")

    @admin.display(description="User", ordering="habit__user__username")
    def get_user(self, obj: CheckIn) -> str:
        return obj.habit.user.username
