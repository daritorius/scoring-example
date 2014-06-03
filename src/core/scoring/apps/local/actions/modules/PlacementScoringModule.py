# -*- coding: utf-8 -*-
from operator import itemgetter
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.scoring_cards.placement_scoring_card import PLACEMENT_TYPE_SCORING_CARD, \
    PLACEMENT_INCOME_SCORING_CARD
from django.utils.translation import ugettext as _


class PlacementScoringModule(BaseScoringModule):
    card = PLACEMENT_TYPE_SCORING_CARD
    card_income = PLACEMENT_INCOME_SCORING_CARD

    min_type_score = -100
    min_income_score = -300
    max_income_score = 300
    max_income_amount = 80000.0

    def calculate_score(self, data):
        placement_type_score = self.calculate_type_score(data)
        placement_income_score = self.calculate_income_score(data)
        print placement_income_score
        total_score = placement_type_score + placement_income_score
        return total_score

    def calculate_type_score(self, data):
        score = self.min_type_score
        if hasattr(data.profile_placement_information, 'placement_type'):
            score = self.card[str(data.profile_placement_information.placement_type[0])]
        return score

    def calculate_income_score(self, data):
        score = self.min_income_score
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income[0])
            if income >= self.max_income_amount:
                score = self.max_income_score
            else:
                for item in sorted(PLACEMENT_INCOME_SCORING_CARD, key=lambda key: PLACEMENT_INCOME_SCORING_CARD[key]):
                    if income < float(item):
                        score = PLACEMENT_INCOME_SCORING_CARD[item]
                        break
        return score