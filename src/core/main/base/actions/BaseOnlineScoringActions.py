# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from django.utils.translation import ugettext_lazy as _


class BaseOnlineScoringActions(BaseActions):
    url = None
    query = None

    def check_address(self, data):
        raise NotImplementedError