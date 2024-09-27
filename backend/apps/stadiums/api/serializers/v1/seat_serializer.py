from django.core.exceptions import ImproperlyConfigured

from rest_framework import serializers

from apps.stadiums.models import Seat


class SeatSerializer(serializers.ModelSerializer):
    match = serializers.SlugRelatedField(slug_field='uuid', read_only=True)

    class Meta:
        model = Seat
        exclude = ('id',)

    def create(self, validated_data):
        raise ImproperlyConfigured('You cant\'t create Seat instances.')

    def update(self, instance, validated_data):
        raise ImproperlyConfigured('You cant\'t update Seat instances.')
