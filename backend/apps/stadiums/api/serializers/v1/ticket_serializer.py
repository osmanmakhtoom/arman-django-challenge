from django.core.exceptions import ImproperlyConfigured

from rest_framework import serializers

from apps.stadiums.models import Ticket
from apps.stadiums.tasks import reserve_seat_task


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='uuid', read_only=True)
    seat = serializers.SlugRelatedField(slug_field='uuid', read_only=True)

    class Meta:
        model = Ticket
        exclude = ('id',)
        read_only_fields = ('uuid', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'user': {'required': False},
        }

    def create(self, validated_data):
        user_uuid = self.context['request'].user.uuid
        seat_uuid = validated_data['seat'].uuid
        task = reserve_seat_task.delay(user_uuid, seat_uuid)
        result = task.get(timeout=10)
        return result

    def update(self, instance, validated_data):
        raise ImproperlyConfigured('You cant\'t update Ticket instances.')
