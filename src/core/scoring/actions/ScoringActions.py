# -*- coding: utf-8 -*-
import json
from core.scoring.apps.country.services.CountryService import CountryService
from core.scoring.apps.local.actions.BaseScoringActions import BaseScoringAction
from core.scoring.apps.local.actions.LocalScoringActions import LocalScoringActions
from core.scoring.plain_models import ScoringPlainModel
from core.scoring.services.ScoringService import ScoringService
from django.utils.translation import ugettext as _


class ScoringActions(BaseScoringAction):
    local_scoring_action = LocalScoringActions()
    scoring_service = ScoringService()
    country_service = CountryService()

    def calculate_scoring(self, data, cleaned_data):
        if hasattr(data, 'user_key'):
            scoring = self.scoring_service.get_item(user_number=getattr(data, 'user_key'))
            if not scoring:
                local_scoring = self._calculate_local_scoring(data)
                save_data = ScoringPlainModel(
                    country=self.country_service.get_item(code=getattr(data, 'country')),
                    rating=local_scoring.rating,
                    local_score=local_scoring,
                    user_data=json.dumps(cleaned_data)
                )
                scoring = self.scoring_service.create(save_data)
        else:
            local_scoring = self._calculate_local_scoring(data)
            save_data = ScoringPlainModel(
                country=self.country_service.get_item(code=getattr(data, 'country')),
                rating=local_scoring.rating,
                local_score=local_scoring,
                user_data=json.dumps(cleaned_data)
            )
            scoring = self.scoring_service.create(save_data)
        return {'score': scoring.local_score.total_score,
                'rating': scoring.rating,
                'user_key': scoring.user_number}

    def _calculate_local_scoring(self, data):
        return self.local_scoring_action.generate_score(data)