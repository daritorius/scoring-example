# -*- coding: utf-8 -*-
from api.exceptions import ApiExceptions
from api.forms.LocalScoringForm import CheckUserKeyForm
from api.forms.MandatoryParametersForm import MandatoryParametersForm
from core.main.base.facades.BaseFacade import BaseFacade
from core.scoring.apps.country.plain_models import CountryPlainModel
from core.scoring.apps.country.services.CountryService import CountryService
from core.scoring.services.ScoringService import ScoringService
from django.utils.translation import ugettext_lazy as _


class BaseScoringFacade(BaseFacade):
    mandatory_parameters = ['country', 'key']
    country_service = CountryService()
    scoring_service = ScoringService()

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