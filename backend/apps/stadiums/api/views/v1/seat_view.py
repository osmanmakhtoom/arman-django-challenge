from django.conf import settings

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.stadiums.api.serializers.v1 import SeatSerializer
from apps.stadiums.models import Seat
from apps.utils.helpers import CacheManager


class SeatView(ListAPIView, RetrieveAPIView):
    serializer_class = SeatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'

    def get_queryset(self):
        """
        Return cached queryset if is not expired else hit to database cache it and return.
        This approach do not any break in system because we do update cached queryset every time updated table data
        """
        cached_queryset = CacheManager(settings.AVAILABLE_SEATS_CACHE_KEY)
        if not cached_queryset.is_expired:
            return cached_queryset.value
        seats = Seat.objects.filter_active(is_reserved=False).select_related('match')
        cached_queryset.period = settings.AVAILABLE_SEATS_CACHE_TIMEOUT
        cached_queryset.value = seats

        return seats
