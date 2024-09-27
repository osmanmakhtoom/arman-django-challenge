from celery import shared_task

from django.conf import settings

from apps.stadiums.models import Match
from apps.utils.helpers import CacheManager


@shared_task
def update_cache_match_info_task():
    cached_queryset = CacheManager(settings.MATCHES_QUERYSET_CACHE_KEY)
    matches = Match.objects.filter_active().select_related('stadium')
    cached_queryset.period = settings.MATCHES_QUERYSET_CACHE_TIMEOUT
    cached_queryset.value = matches
