from django.conf.urls import url
from views import(
    WeekViewSet, BetView, AddBetView, BetHistoryViewSet, SongViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('week', WeekViewSet)
router.register('history', BetHistoryViewSet, base_name='history')
router.register('song', SongViewSet, base_name='song')

urlpatterns = [
    url(r'createbet/$', BetView.as_view(), name='bet'),
    url(r'addbet/$', AddBetView.as_view(), name='bet'),
]
urlpatterns += router.urls
