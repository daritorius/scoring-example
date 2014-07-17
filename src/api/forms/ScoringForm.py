# -*- coding: utf-8 -*-
from core.scoring.apps.local.plain_models import ProfilePassportPlainModel, \
    OfficialAddressPlainModel, RealAddressPlainModel, PersonalInformationPlainModel, \
    PlacementPlainModel, AdditionalIncomePlainModel, ChargesPlainModel, CreditChargesPlainModel, AssetsPlainModel, \
    IntegerFieldsPlainModel, FloatFieldsPlainModel
from django import forms
from django.utils.translation import ugettext as _


class CheckUserKeyForm(forms.Form):
    user_key = forms.CharField(max_length=255, required=False)


class ScoringForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ScoringForm, self).__init__(*args, **kwargs)
        fields = ProfilePassportPlainModel.fields + \
                 OfficialAddressPlainModel.fields + \
                 RealAddressPlainModel.fields + \
                 PersonalInformationPlainModel.fields + \
                 PlacementPlainModel.fields + \
                 AdditionalIncomePlainModel.fields + \
                 ChargesPlainModel.fields + \
                 CreditChargesPlainModel.fields + \
                 AssetsPlainModel.fields + \
                 ['country', 'profile_birthday', 'key', 'user_key', 'profile_addresses_similar']
        for field in fields:
            if field in IntegerFieldsPlainModel().fields:
                self.fields[field] = forms.IntegerField(required=False)
            elif field in FloatFieldsPlainModel().fields:
                self.fields[field] = forms.FloatField(required=False)
            else:
                self.fields[field] = forms.CharField(max_length=255, required=False)