from celery import shared_task

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction

from apps.stadiums.models import Ticket, Seat
from apps.utils.helpers import CacheManager


User = get_user_model()


@shared_task
def reserve_seat_task(seat_uuid, user_uuid):
    cached_queryset = CacheManager(settings.AVAILABLE_SEATS_CACHE_KEY)
    with transaction.atomic():
        seat = Seat.objects.filter_active(is_reserved=False).select_related('match').select_for_update().get(uuid=seat_uuid)
        user = User.objects.filter_active().get(uuid=user_uuid)
        seat.is_reserved = True
        seat.save()
        # Here we do not activate ticket because there are no transactions, we activate it after successful transaction
        ticket = Ticket.objects.create(seat=seat, user=user)
        cached_queryset.period = settings.AVAILABLE_SEATS_CACHE_TIMEOUT
        cached_queryset.value = Seat.objects.filter_active(is_reserved=False).select_related('match')
        return ticket
