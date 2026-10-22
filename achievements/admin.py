from django.contrib import admin

from .models import Achievement, UserAchievement


class UserAchievementInline(admin.TabularInline):
    model = UserAchievement
    extra = 0
    readonly_fields = ("earned_at",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "required_checkins", "bonus_xp")
    search_fields = ("name",)
    inlines = [UserAchievementInline]


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ("user", "achievement", "earned_at")
    list_filter = ("achievement",)
    search_fields = ("user__username", "achievement__name")
    readonly_fields = ("earned_at",)
