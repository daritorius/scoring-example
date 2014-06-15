# -*- coding: utf-8 -*-
from core.main.base.facades.BaseFacade import Singleton
from django.utils.translation import ugettext as _


class BaseScoringModule(object):
    __metaclass__ = Singleton
    cards = None

    def calculate_score(self, data):
        raise NotImplementedError