from django.conf.urls import url
from views import current_week, NormalBetViewSet


urlpatterns = [
    url(r'1x2/$', NormalBetViewSet.as_view({'post': 'create'}),
        name='normal_bet'),
    url(r'week/$', current_week, name='current_week'),
]
