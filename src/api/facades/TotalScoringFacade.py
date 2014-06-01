# -*- coding: utf-8 -*-
from api.exceptions import ApiExceptions
from api.facades.BaseScoringFacade import BaseScoringFacade
from core.main.base.facades.BaseFacade import BaseFacade
from core.scoring.apps.country.services.CountryService import CountryService
from django.utils.translation import ugettext_lazy as _


class TotalScoringFacade(BaseScoringFacade, BaseFacade):

    def process_request(self, data):
        self.check_mandatory_parameters(data)
        return True