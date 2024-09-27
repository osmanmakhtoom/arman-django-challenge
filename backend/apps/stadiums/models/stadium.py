from django.db import models

from apps.utils.model_mixins import IsActiveMixin, TimestampedMixin, UUIDMixin
from apps.utils.managers import FilterActiveManager


class Stadium(TimestampedMixin, IsActiveMixin, UUIDMixin):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    capacity = models.IntegerField(default=0)

    objects = FilterActiveManager()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Stadium: name={self.name}, capacity={self.capacity}>'
