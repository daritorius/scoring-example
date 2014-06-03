# -*- coding: utf-8 -*-
from core.scoring.apps.local.actions.BaseScoringActions import BaseScoringAction
from core.scoring.apps.local.actions.modules.AgeScoringModule import AgeScoringModule
from core.scoring.apps.local.actions.modules.PlacementScoringModule import PlacementScoringModule
from django.utils.translation import ugettext_lazy as _


class LocalScoringActions(BaseScoringAction):
    age_scoring_module = AgeScoringModule()
    placement_scoring_module = PlacementScoringModule()

    def generate_score(self, data):
        age_score = self.age_scoring_module.calculate_score(data)
        placement_score = self.placement_scoring_module.calculate_score(data)
        return 'A'

    def calculate_placement_score(self, data):
        if data.placement_information:
            score = 0
        else:
            score = 0
        return score