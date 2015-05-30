from django.conf.urls import url
from views import NormalBetView, current_week

urlpatterns = [
    url(r'1x2$', NormalBetView.as_view(), name='normal_bet'),
    url(r'week$', current_week, name='current_week'),
]
