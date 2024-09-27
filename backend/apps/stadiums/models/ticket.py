from django.contrib.auth import get_user_model
from django.db import models

from apps.utils.model_mixins import IsActiveMixin, TimestampedMixin, UUIDMixin
from apps.utils.managers import FilterActiveManager

from apps.stadiums.models import Seat


class Ticket(TimestampedMixin, IsActiveMixin, UUIDMixin):
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT, related_name='tickets')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='tickets')

    objects = FilterActiveManager()

    def __str__(self):
        return f'Ticket for {self.user.uuid} - {self.seat}'

    def __repr__(self):
        return f'<Ticket: user={self.user.uuid}, {self.seat}, {self.created_at}>'
