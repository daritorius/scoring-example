# -*- coding: utf-8 -*-
from api.exceptions import ApiExceptions
from api.facades.BaseScoringFacade import BaseScoringFacade
from api.forms.ScoringForm import ScoringForm
from django.utils.translation import ugettext_lazy as _


class OnlineScoringFacade(BaseScoringFacade):

    def process_request(self, data):
        self.check_mandatory_parameters(data)
        self.process_prevent_detection(data)
        form = ScoringForm(data)
        if form.is_valid():
            user_data = self.generate_user_data(self.clean_data(form.cleaned_data))
            scoring = self.online_scoring_actions.calculate_online_scoring(user_data)
            return scoring
        else:
            raise ApiExceptions(u'Wrong request: %s' % form.errors.as_text)