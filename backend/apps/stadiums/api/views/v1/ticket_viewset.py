from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.stadiums.api.serializers.v1 import TicketSerializer
from apps.stadiums.models import Ticket


@method_decorator(cache_page(60 * 10), name='dispatch')
class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user).select_related('user', 'seat')
