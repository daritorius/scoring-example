# -*- coding: utf-8 -*-
from api.facades.BaseScoringFacade import BaseScoringFacade
from django.utils.translation import ugettext_lazy as _


class IndexFacade(BaseScoringFacade):

    def calculate_scoring(self, data, request):
        user_data = self.generate_user_data(self.clean_data(data))
        user_data.country = 'ua'
        scoring = self.scoring_actions.calculate_web_scoring(user_data)
        return scoring