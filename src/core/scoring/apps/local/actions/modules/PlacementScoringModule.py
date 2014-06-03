# -*- coding: utf-8 -*-
from core.scoring.apps.local.plain_models import ChargesPlainModel
from django.utils.translation import ugettext as _
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.scoring_cards.placement_scoring_card import PLACEMENT_TYPE_SCORING_CARD, \
    PLACEMENT_INCOME_SCORING_CARD, PLACEMENT_CLEAN_INCOME_SCORING_CARD


class PlacementScoringModule(BaseScoringModule):
    card = PLACEMENT_TYPE_SCORING_CARD
    card_income = PLACEMENT_INCOME_SCORING_CARD
    card_clean_income = PLACEMENT_CLEAN_INCOME_SCORING_CARD

    min_type_score = -100
    min_income_score = -300
    max_income_score = 300
    max_income_amount = 80000.0
    min_clean_income_score = -300
    max_clean_income_score = -300
    max_clean_income_amount = 10000.0

    def calculate_score(self, data):
        placement_type_score = self.calculate_type_score(data)
        placement_income_score = self.calculate_income_score(data)
        placement_clean_income = self.calculate_clean_income(data)
        print placement_type_score
        print placement_income_score
        print placement_clean_income
        total_score = placement_type_score + placement_income_score
        return total_score

    def calculate_type_score(self, data):
        score = self.min_type_score
        if hasattr(data.profile_placement_information, 'placement_type'):
            score = self.card[str(data.profile_placement_information.placement_type[0])]
        return score

    def calculate_income_score(self, data):
        score = self.min_income_score
        income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income[0])
        if income >= self.max_income_amount:
            score = self.max_income_score
        else:
            for item in sorted(self.card_income, key=lambda key: self.card_income[key]):
                if income < float(item):
                    score = self.card_income[item]
                    break
        return score

    def calculate_clean_income(self, data):
        score = self.min_clean_income_score
        charges = income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income[0])
        for item in ChargesPlainModel.fields:
            if hasattr(data.profile_charges, item):
                charges += float(getattr(data.profile_charges, item))
        clean_income = income - charges
        if clean_income >= self.max_clean_income_amount:
            score = self.max_clean_income_score
        else:
            for item in sorted(self.card_clean_income, key=lambda key: self.card_clean_income[key]):
                if income < float(item):
                    score = self.card_clean_income[item]
                    break
        return score