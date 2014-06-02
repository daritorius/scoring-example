# -*- coding: utf-8 -*-
from api.exceptions import ApiExceptions
from api.forms.MandatoryParametersForm import MandatoryParametersForm
from core.main.base.facades.BaseFacade import BaseFacade
from core.scoring.apps.country.plain_models import CountryPlainModel
from core.scoring.apps.country.services.CountryService import CountryService
from django.utils.translation import ugettext_lazy as _


class BaseScoringFacade(BaseFacade):
    mandatory_parameters = ['country', 'key']
    country_service = CountryService()

    def check_mandatory_parameters(self, data):
        for parameter in self.mandatory_parameters:
            if not data.get(parameter, None):
                raise ApiExceptions(u"Need '%s' parameter in request" % parameter)
        self.check_key_country(data)

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