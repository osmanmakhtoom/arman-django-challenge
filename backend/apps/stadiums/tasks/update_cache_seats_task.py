from celery import shared_task

from django.conf import settings

from apps.stadiums.models import Seat
from apps.utils.helpers import CacheManager


@shared_task
def update_cache_seats_task():
    cached_queryset = CacheManager(settings.AVAILABLE_SEATS_CACHE_KEY)
    seats = Seat.objects.filter_active().select_related('match')
    cached_queryset.period = settings.AVAILABLE_SEATS_CACHE_TIMEOUT
    cached_queryset.value = seats
