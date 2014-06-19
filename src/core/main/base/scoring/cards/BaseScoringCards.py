# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from django.utils.translation import ugettext as _


class BaseScoringCardActions(BaseActions):
    service = None

    max_score = 300
    min_score = -300

    def get_card(self):
        self.service.get_all(order_by='value')