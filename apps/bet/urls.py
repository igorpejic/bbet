from django.conf.urls import url
from views import WeekViewSet, NormalBetViewSet, BetView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('week', WeekViewSet)

urlpatterns = [
    url(r'1x2/$', NormalBetViewSet.as_view(),
        name='normal_bet'),
    url(r'bet/$', BetView.as_view(), name='bet'),
]
urlpatterns += router.urls
