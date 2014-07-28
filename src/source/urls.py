from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('web.scoring.urls', namespace='main')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^sadmin/', include(admin.site.urls)),
)
