from django.conf.urls import url
from views import WeekViewSet, NormalBetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('week', WeekViewSet)

urlpatterns = [
    url(r'1x2/$', NormalBetViewSet.as_view({'post': 'create'}),
        name='normal_bet'),
]
urlpatterns += router.urls
