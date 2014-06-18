# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class BasePlainModel(object):
    fields = []
    default_fields = ['date_create', 'date_update', 'is_deleted']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.fields or key in self.default_fields:
                setattr(self, key, value)