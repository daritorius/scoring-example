# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from core.main.base.facades.BaseFacade import Singleton
from django.utils.translation import ugettext as _


class BaseScoringAction(BaseActions):

    def generate_score(self, data):
        raise NotImplementedError