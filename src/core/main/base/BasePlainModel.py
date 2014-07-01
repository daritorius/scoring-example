# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class BasePlainModel(object):
    base_fields = ['id', 'date_create', 'date_update', 'is_deleted']
    fields = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if self.is_key_in_fields(key):
                setattr(self, key, value)

    def is_key_in_fields(self, key):
        if self.is_key_in_external_fields(key) or self.is_key_in_base_fields(key):
            return True
        return False

    def is_key_in_base_fields(self, key):
        if key in self.base_fields or key.split('__')[0] in self.base_fields:
            return True
        return False

    def is_key_in_external_fields(self, key):
        if key in self.fields or key.split('__')[0] in self.fields:
            return True
        return False