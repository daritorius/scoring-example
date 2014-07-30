# -*- coding: utf-8 -*-
from api.forms.ScoringForm import ScoringForm
from django.utils.translation import ugettext_lazy as _
from api.exceptions import ApiExceptions
from api.facades.BaseScoringFacade import BaseScoringFacade
from core.scoring.actions.ScoringActions import ScoringActions


class LocalScoringFacade(BaseScoringFacade):

    def process_request(self, data):
        self.check_mandatory_parameters(data)
        # self.process_prevent_detection(data)
        form = ScoringForm(data)
        if form.is_valid():
            user_data = self.generate_user_data(self.clean_data(form.cleaned_data))
            scoring = self.scoring_actions.calculate_scoring(user_data, form.cleaned_data)
            return scoring
        else:
            raise ApiExceptions(u'Wrong request: %s' % form.errors.as_text)

    def clean_data(self, data):
        del_keys = []
        for key, value in data.iteritems():
            if data[key] is None or data[key] == '':
                del_keys.append(key)
        for key in del_keys:
            del data[key]
        return data