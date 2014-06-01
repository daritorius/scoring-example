# -*- coding: utf-8 -*-
from api.facades.BaseScoringFacade import BaseScoringFacade
from core.main.base.facades.BaseFacade import BaseFacade
from django.utils.translation import ugettext_lazy as _


class LocalScoringFacade(BaseScoringFacade, BaseFacade):

    def process_request(self, data):
        self.check_mandatory_parameters(data)
        return 'A'