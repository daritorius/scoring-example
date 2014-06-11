# -*- coding: utf-8 -*-
from core.scoring.apps.local.plain_models import ProfilePainModel, ProfilePassportPlainModel, \
    OfficialAddressPlainModel, RealAddressPlainModel, PersonalInformationPlainModel, \
    PlacementPlainModel, AdditionalIncomePlainModel, ChargesPlainModel, CreditChargesPlainModel, AssetsPlainModel
from django import forms
from django.utils.translation import ugettext as _


class LocalScoringForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LocalScoringForm, self).__init__(*args, **kwargs)
        fields = ProfilePassportPlainModel.fields + \
                 OfficialAddressPlainModel.fields + \
                 RealAddressPlainModel.fields + \
                 PersonalInformationPlainModel.fields + \
                 PlacementPlainModel.fields + \
                 AdditionalIncomePlainModel.fields + \
                 ChargesPlainModel.fields + \
                 CreditChargesPlainModel.fields + \
                 AssetsPlainModel.fields
        for field in fields:
            self.fields[field] = forms.CharField(max_length=255, required=False)