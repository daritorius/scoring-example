# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from core.main.base.actions.BaseActions import BaseActions


class BaseOnlineScoringActions(BaseActions):
    url = None
    query = None
    base_path = ''
    port = 80
    method = 'GET'
    format = 'json'