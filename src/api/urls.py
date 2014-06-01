# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from api.views import total_scoring_view, plain_view, local_scoring_view
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^total/$', total_scoring_view, name='total_scoring_request'),
    url(r'^local/$', local_scoring_view, name='local_scoring_request'),
    url(r'^$', plain_view, name='plain_request'),
)