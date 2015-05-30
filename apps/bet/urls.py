from django.conf.urls import url
from views import NormalBetView

urlpatterns = [
    url(r'1x2$', NormalBetView.as_view(), name='normal_bet'),
]
