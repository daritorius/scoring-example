# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _


class MandatoryParametersForm(forms.Form):
    country = forms.CharField(max_length=255)
    key = forms.CharField(max_length=255)