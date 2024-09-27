from django.core.exceptions import ImproperlyConfigured

from rest_framework import serializers

from apps.stadiums.models import Stadium


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        exclude = ('id',)

    def create(self, validated_data):
        raise ImproperlyConfigured('You cant\'t create Stadium instances.')

    def update(self, instance, validated_data):
        raise ImproperlyConfigured('You cant\'t update Stadium instances.')
