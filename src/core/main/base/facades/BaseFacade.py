# -*- coding: utf-8 -*-
from core.main.base.modules.Singleton import Singleton
from django.utils.translation import ugettext_lazy as _


class BaseFacade(object):
    __metaclass__ = Singleton