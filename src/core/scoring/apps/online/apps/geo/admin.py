# -*- coding: utf-8 -*-
from core.scoring.apps.online.apps.geo.models import GeoGoogle, GeoYandex
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


admin.site.register(GeoGoogle)
admin.site.register(GeoYandex)