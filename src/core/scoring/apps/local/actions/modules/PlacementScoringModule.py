# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from core.scoring.apps.local.plain_models import ChargesPlainModel
from core.scoring.apps.local.scoring_cards.PlacementInformationCards import PlacementInformationCards
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule


class PlacementScoringModule(BaseScoringModule):
    cards = PlacementInformationCards()

    def calculate_score(self, data):
        placement_type_score = self.calculate_type_score(data)
        print 'placement type score: %s' % placement_type_score
        placement_income_score = self.calculate_income_score(data)
        print 'placement income score: %s' % placement_income_score
        placement_clean_income = self.calculate_clean_income(data)
        print 'placement clean income: %s' % placement_clean_income
        total_score = placement_type_score + placement_income_score + placement_clean_income
        employment_score = self.calculate_score_for_employment_user(data)
        return total_score

    def calculate_score_for_employment_user(self, data):
        if hasattr(data.profile_placement_information, 'placement_type'):
            pass

    def calculate_type_score(self, data):
        score = self.cards.min_type_score
        if hasattr(data.profile_placement_information, 'placement_type'):
            score = self.cards.get_placement_type_card()[str(data.profile_placement_information.placement_type[0])]
        return score

    def calculate_income_score(self, data):
        score = self.cards.min_income_score
        income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income[0])
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            income += getattr(data.profile_placement_information, 'placement_additional_income')[0]
        if income >= self.cards.max_income_amount:
            score = self.cards.max_income_score
        else:
            for item in sorted(self.cards.get_placement_income_card(),
                               key=lambda key: self.cards.get_placement_income_card()[key]):
                if income < float(item):
                    score = self.cards.get_placement_income_card()[item]
                    break
        return score

    def calculate_clean_income(self, data):
        score = self.cards.min_clean_income_score
        charges = income = 0
        if hasattr(data.profile_placement_information, 'placement_income'):
            income = float(data.profile_placement_information.placement_income[0])
        if hasattr(data.profile_placement_information, 'placement_additional_income'):
            income += getattr(data.profile_placement_information, 'placement_additional_income')[0]
        for item in ChargesPlainModel.fields:
            if hasattr(data.profile_charges, item):
                charges += float(getattr(data.profile_charges, item)[0])
        clean_income = income - charges
        if clean_income >= self.cards.max_clean_income_amount:
            score = self.cards.max_clean_income_score
        else:
            for item in sorted(self.cards.get_placement_clean_income_card(),
                               key=lambda key: self.cards.get_placement_clean_income_card()[key]):
                if income < float(item):
                    score = self.cards.get_placement_clean_income_card()[item]
                    break
        return score