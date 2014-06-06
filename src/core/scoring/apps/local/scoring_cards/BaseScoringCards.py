# -*- coding: utf-8 -*-
from core.main.base.facades.BaseFacade import Singleton
from django.utils.translation import ugettext as _


class BaseScoringCards(object):
    __metaclass__ = Singleton

    max_score = 300
    min_score = -300