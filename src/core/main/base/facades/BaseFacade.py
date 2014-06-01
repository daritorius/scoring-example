# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseFacade(object):
    __metaclass__ = Singleton