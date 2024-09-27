from django.db import models

from apps.stadiums.models import Stadium

from apps.utils.model_mixins import IsActiveMixin, TimestampedMixin, UUIDMixin
from apps.utils.managers import FilterActiveManager


class Match(TimestampedMixin, IsActiveMixin, UUIDMixin):
    stadium = models.ForeignKey(Stadium, on_delete=models.PROTECT, related_name='matches')
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    match_date = models.DateTimeField()

    objects = FilterActiveManager()

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} @ {self.stadium.name} on {self.match_date}'

    def __repr__(self):
        return f'<Match: home={self.home_team}, away={self.away_team}, date={self.match_date}, stadium={self.stadium.name}>'
