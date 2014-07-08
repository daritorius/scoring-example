# -*- coding: utf-8 -*-
from core.main.base.modules.Singleton import Singleton
from django.utils.translation import ugettext as _


class BaseActions(object):
    __metaclass__ = Singleton