from django.conf.urls import url
from apps.social.views import (home, validation_sent, logout, done,
                               ajax_auth, require_email)


urlpatterns = [
    url(r'^$', home),
    url(r'^login/$', home),
    url(r'^email-sent/', validation_sent),
    url(r'^logout/$', logout),
    url(r'^done/$', done, name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', ajax_auth,
        name='ajax-auth'),
    url(r'^email/$', require_email, name='require_email'),
]
