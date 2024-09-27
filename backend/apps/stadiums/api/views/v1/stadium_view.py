from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.stadiums.api.serializers.v1 import StadiumSerializer
from apps.stadiums.models import Stadium


@method_decorator(cache_page(60 * 10), name='dispatch')
class StadiumView(ListAPIView, RetrieveAPIView):
    queryset = Stadium.objects.filter_active()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
