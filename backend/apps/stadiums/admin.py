from django.contrib import admin

from apps.stadiums.models import Stadium, Match, Seat, Ticket
from apps.stadiums.tasks import update_cache_match_info_task, update_cache_seats_task


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'location')
    search_fields = ('name', 'description', 'location', 'uuid')
    date_hierarchy = 'created_at'


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('stadium', 'home_team', 'away_team', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'home_team', 'away_team')
    search_fields = ('stadium__name', 'home_team', 'away_team', 'uuid')
    date_hierarchy = 'created_at'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        update_cache_match_info_task.delay()


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'match', 'is_reserved', 'price', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_reserved', 'match', 'price')
    search_fields = ('seat_number', 'match__home_team', 'match__away_team', 'price', 'uuid')
    date_hierarchy = 'created_at'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        update_cache_seats_task.delay()


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'seat', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'seat', 'user')
    search_fields = ('user__email', 'seat__price', 'uuid')
    date_hierarchy = 'created_at'
