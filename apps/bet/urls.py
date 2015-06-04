from django.conf.urls import url
from views import normal_bet, current_week

urlpatterns = [
    url(r'1x2/$', normal_bet, name='normal_bet'),
    url(r'week/$', current_week, name='current_week'),
]
