# -*- coding: utf-8 -*-
from core.main.base.actions.BaseOnlineScoringActions import BaseOnlineScoringActions
from django.utils.translation import ugettext_lazy as _


class GoogleActions(BaseOnlineScoringActions):
    url = 'maps.google.com/maps/geo/'
    query = 'q'