# -*- coding: utf-8 -*-
from core.scoring.apps.online.apps.geo.actions.BaseGeoActions import BaseGeoActions
from django.utils.translation import ugettext_lazy as _


class GeoYandexActions(BaseGeoActions):
    url = 'http://geocode-maps.yandex.ru/1.x/'
    base_path = '/'
    query = 'geocode'