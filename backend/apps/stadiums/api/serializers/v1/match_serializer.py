from django.core.exceptions import ImproperlyConfigured

from rest_framework import serializers

from apps.stadiums.models import Match


class MatchSerializer(serializers.ModelSerializer):
    stadium = serializers.SlugRelatedField(slug_field='uuid', read_only=True)

    class Meta:
        model = Match
        exclude = ('id',)

    def create(self, validated_data):
        raise ImproperlyConfigured('You cant\'t create Match instances.')

    def update(self, instance, validated_data):
        raise ImproperlyConfigured('You cant\'t update Match instances.')
