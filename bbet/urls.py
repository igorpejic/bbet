from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apps.bet.urls')),
    url(r'^app/', views.index, name='index'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^social/', include('social.apps.django_app.urls',
                             namespace='social'))
)
