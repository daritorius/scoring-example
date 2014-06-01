# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class BasePlainModel(object):
    fields = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.fields:
                setattr(self, key, value)