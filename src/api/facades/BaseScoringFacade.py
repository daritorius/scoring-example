# -*- coding: utf-8 -*-
from api.exceptions import ApiExceptions
from api.forms.MandatoryParametersForm import MandatoryParametersForm
from api.forms.ScoringForm import CheckUserKeyForm
from core.main.base.facades.BaseFacade import BaseFacade
from core.scoring.actions.ScoringActions import ScoringActions
from core.scoring.apps.country.plain_models import CountryPlainModel
from core.scoring.apps.country.services.CountryService import CountryService
from core.scoring.apps.local.plain_models import ProfilePassportPlainModel, OfficialAddressPlainModel, \
    RealAddressPlainModel, PersonalInformationPlainModel, PlacementPlainModel, AdditionalIncomePlainModel, \
    ChargesPlainModel, CreditChargesPlainModel, AssetsPlainModel, ProfilePainModel
from core.scoring.apps.online.actions.OnlinePreventActions import OnlinePreventActions
from core.scoring.apps.online.actions.OnlineScoringActions import OnlineScoringActions
from core.scoring.services.ScoringService import ScoringService
from django.utils.translation import ugettext_lazy as _


class BaseScoringFacade(BaseFacade):
    mandatory_parameters = ['country', 'key']
    country_service = CountryService()
    scoring_service = ScoringService()
    scoring_actions = ScoringActions()
    online_prevent_actions = OnlinePreventActions()
    online_scoring_actions = OnlineScoringActions()

    def check_mandatory_parameters(self, data):
        for parameter in self.mandatory_parameters:
            if not data.get(parameter, None):
                raise ApiExceptions(u"Need '%s' parameter in request" % parameter)
        self.check_key_country(data)
        self.check_user_key(data)

    def check_key_country(self, data):
        form = MandatoryParametersForm(data)
        if form.is_valid():
            check_data = CountryPlainModel(code=form.cleaned_data.get('country', None),
                                           key=form.cleaned_data.get('key', None))
            result = self.country_service.get_item(**check_data.__dict__)
            if not result:
                raise ApiExceptions(u"The key does not match the country code")
            return result
        else:
            raise ApiExceptions(u"Request is not valid")

    def check_user_key(self, data):
        form = CheckUserKeyForm(data)
        if form.is_valid():
            if form.cleaned_data.get('user_key', None):
                scoring = self.scoring_service.get_item(user_number=form.cleaned_data.get('user_key', None))
                if not scoring:
                    raise ApiExceptions(u"No user with such key")
        else:
            raise ApiExceptions(u"User Key is not valid")

    def generate_user_data(self, data):
        profile_passport_data = ProfilePassportPlainModel(**data)
        official_address_data = OfficialAddressPlainModel(**data)
        real_address_data = RealAddressPlainModel(**data)
        personal_profile_data = PersonalInformationPlainModel(**data)
        placement_profile_data = PlacementPlainModel(**data)
        additional_income_data = AdditionalIncomePlainModel(**data)
        charges_profile_data = ChargesPlainModel(**data)
        credit_charges_profile_data = CreditChargesPlainModel(**data)
        assets_profile_data = AssetsPlainModel(**data)
        profile_data = ProfilePainModel(
            profile_passport_information=profile_passport_data,
            profile_official_address=official_address_data,
            profile_real_address=real_address_data,
            profile_personal_information=personal_profile_data,
            profile_placement_information=placement_profile_data,
            profile_additional_income=additional_income_data,
            profile_charges=charges_profile_data,
            profile_credit_charges=credit_charges_profile_data,
            profile_assets=assets_profile_data,
            **data)
        return profile_data

    def clean_data(self, data):
        del_keys = []
        for key, value in data.iteritems():
            if data[key] is None or data[key] == '':
                del_keys.append(key)
        for key in del_keys:
            del data[key]
        return data

    def process_prevent_detection(self, data):
        if self.online_prevent_actions.check_person(data):
            raise ApiExceptions(u"Error while calculating your score")