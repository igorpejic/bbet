from django.conf.urls import url
from api import(
    LastWeekViewSet, BetView, AddBetView, BetHistoryViewSet, SongViewSet,
    PositionViewSet, WeekViewSet, RegisterView,
    GoogleAuthView,
    FacebookAuthView,
    SocialUserView,
    AbsoluteLeaderboardView,
    MyBetsViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('lastweek', LastWeekViewSet, base_name='lastweek')
router.register('history', BetHistoryViewSet, base_name='history')
router.register('song', SongViewSet, base_name='song')
router.register('week', WeekViewSet, base_name='week')
router.register('mybets', MyBetsViewSet, base_name='mybets')

urlpatterns = [
    url(r'bet/$', BetView.as_view(), name='bet'),
    url(r'addbet/$', AddBetView.as_view(), name='bet'),
    url(r'position/(?P<pk>[0-9]+)/$', PositionViewSet.as_view(),
        name='position'),
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'login/google-oauth2/$', GoogleAuthView.as_view()),
    url(r'login/facebook/$', FacebookAuthView.as_view()),
    url(r'socialuser/$', SocialUserView.as_view()),
    url(r'leaderboard/$', AbsoluteLeaderboardView.as_view(), name='leaderboard-absolute'),
]
urlpatterns += router.urls
