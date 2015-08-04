from django.conf.urls import url
from views import(
    LastWeekViewSet, BetView, AddBetView, BetHistoryViewSet, SongViewSet,
    PositionViewSet, WeekViewSet, RegisterView,
    SocialAuthView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('lastweek', LastWeekViewSet)
router.register('history', BetHistoryViewSet, base_name='history')
router.register('song', SongViewSet, base_name='song')
router.register('week', WeekViewSet, base_name='week')

urlpatterns = [
    url(r'bet/$', BetView.as_view(), name='bet'),
    url(r'addbet/$', AddBetView.as_view(), name='bet'),
    url(r'position/(?P<pk>[0-9]+)/$', PositionViewSet.as_view(),
        name='position'),
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'login/$', SocialAuthView.as_view()),
]
urlpatterns += router.urls
