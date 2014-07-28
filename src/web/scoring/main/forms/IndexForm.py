# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class IndexForm(forms.Form):
    profile_third_name = forms.CharField(max_length=255, required=True, label=_(u'Фамилия'))
    profile_first_name = forms.CharField(max_length=255, required=True, label=_(u'Имя'))
    profile_second_name = forms.CharField(max_length=255, required=True, label=_(u'Отчество'))
    profile_birthday = forms.CharField(max_length=255, required=True, label=_(u'Дата рождения (дд-мм-гггг)'))