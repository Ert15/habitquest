from django.contrib import admin

from .models import Challenge, Participation


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1
    readonly_fields = ("joined_at",)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "creator",
        "start_date",
        "end_date",
        "is_public",
        "get_participants_count",
    )
    list_filter = ("is_public", "start_date")
    search_fields = ("title", "creator__username")
    date_hierarchy = "start_date"
    inlines = [ParticipationInline]

    @admin.display(description="Participants")
    def get_participants_count(self, obj: Challenge) -> int:
        return obj.participations.count()


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ("user", "challenge", "score", "joined_at")
    list_filter = ("challenge",)
    search_fields = ("user__username", "challenge__title")
    readonly_fields = ("joined_at",)
