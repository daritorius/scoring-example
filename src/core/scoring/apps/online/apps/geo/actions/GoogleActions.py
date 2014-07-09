# -*- coding: utf-8 -*-
import json
import urllib
import urllib2
from core.main.base.actions.BaseOnlineScoringActions import BaseOnlineScoringActions
from django.utils.translation import ugettext_lazy as _


class GoogleActions(BaseOnlineScoringActions):
    url = 'https://maps.googleapis.com/maps/api/geocode/%s' % BaseOnlineScoringActions.format
    query = 'address'
    source = 'google'