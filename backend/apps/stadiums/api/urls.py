from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.stadiums.api.views.v1 import (
    StadiumView as StadiumViewV1,
    MatchView as MatchViewV1,
    SeatView as SeatViewV1,
    TicketViewSet as TicketViewSetV1,
)

router = DefaultRouter(trailing_slash=False)
router.register('v1/tickets', TicketViewSetV1, basename='tickets')

urlpatterns = router.urls + [
    path('v1/stadiums', StadiumViewV1.as_view(), name='stadiums'),
    path('v1/matches', MatchViewV1.as_view(), name='matches'),
    path('v1/seats', SeatViewV1.as_view(), name='seats'),
]
