# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from django.utils.translation import ugettext as _


class BaseScoringCardActions(BaseActions):
    service = None

    max_score = 300
    min_score = -300

    def get_card(self):
        return self.service.get_all(order_by='value')

    def get_min_score(self):
        return self.service.get_all(order_by='value')[0].value

    def get_max_score(self):
        return self.service.get_all(order_by='-value')[0].value

    def get_min_key(self):
        return self.service.get_all(order_by='value')[0].key

    def get_max_key(self):
        return self.service.get_all(order_by='-value')[0].key