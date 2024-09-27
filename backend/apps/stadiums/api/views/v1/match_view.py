from django.conf import settings

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.stadiums.api.serializers.v1 import MatchSerializer
from apps.stadiums.models import Match
from apps.utils.helpers import CacheManager


class MatchView(ListAPIView, RetrieveAPIView):
    serializer_class = MatchSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'

    def get_queryset(self):
        """
        Return cached queryset if is not expired else hit to database cache it and return.
        This approach do not any break in system because we do update cached queryset every time updated table data
        """
        cached_queryset = CacheManager(settings.MATCHES_QUERYSET_CACHE_KEY)
        if not cached_queryset.is_expired:
            return cached_queryset.value
        matches = Match.objects.filter_active().select_related('stadium')
        cached_queryset.period = settings.MATCHES_QUERYSET_CACHE_TIMEOUT
        cached_queryset.value = matches

        return matches
