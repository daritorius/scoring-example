# -*- coding: utf-8 -*-
from core.scoring.apps.online.apps.geo.actions.BaseGeoActions import BaseGeoActions
from django.utils.translation import ugettext_lazy as _


class GoogleActions(BaseGeoActions):
    url = 'https://maps.googleapis.com/maps/api/geocode/%s' % BaseGeoActions.format
    query = 'address'
    source = 'google'