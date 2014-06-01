# -*- coding: utf-8 -*-
from api.exceptions import ApiTypeError
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View


class PlainView(View):
    def dispatch(self, request, *args, **kwargs):
        raise ApiTypeError(u'Need 1 or more keys in your request')