from django.db import models

from apps.utils.model_mixins import IsActiveMixin, TimestampedMixin, UUIDMixin
from apps.utils.managers import FilterActiveManager

from apps.stadiums.models import Match


class Seat(TimestampedMixin, IsActiveMixin, UUIDMixin):
    match = models.ForeignKey(Match, on_delete=models.PROTECT, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_reserved = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    objects = FilterActiveManager()

    def __str__(self):
        return f'{self.seat_number} for {self.match}'

    def __repr__(self):
        return f'<Seat: number={self.seat_number}, match={self.match}>'
