from django.conf.urls import url
from views import WeekViewSet, BetView, AddBetView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('week', WeekViewSet)

urlpatterns = [
    url(r'createbet/$', BetView.as_view(), name='bet'),
    url(r'addbet/$', AddBetView.as_view(), name='bet'),
]
urlpatterns += router.urls
