# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from web.scoring.main.views import index_view


urlpatterns = patterns('',
    url(r'^$', index_view, name='index_page'),
)