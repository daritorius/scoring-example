# -*- coding: utf-8 -*-
from core.scoring.apps.local.actions.modules.AssetScoringModule import AssetScoringModule
from core.scoring.apps.local.actions.modules.CreditScoringModule import CreditScoringModule
from core.scoring.apps.local.plain_models import LocalScoringPlainModel
from core.scoring.apps.local.services.LocalScoringService import LocalScoringService
from core.scoring.scoring_cards.MainLocalScoringCard import MainLocalScoringCard
from django.utils.translation import ugettext_lazy as _
from core.scoring.apps.local.actions.BaseScoringActions import BaseScoringAction
from core.scoring.apps.local.actions.modules.AgeScoringModule import AgeScoringModule
from core.scoring.apps.local.actions.modules.PersonalScoringModule import PersonalScoringModule
from core.scoring.apps.local.actions.modules.PlacementScoringModule import PlacementScoringModule


class LocalScoringActions(BaseScoringAction):
    main_local_scoring_card = MainLocalScoringCard()
    age_scoring_module = AgeScoringModule()
    placement_scoring_module = PlacementScoringModule()
    personal_scoring_module = PersonalScoringModule()
    asset_scoring_module = AssetScoringModule()
    loan_scoring_module = CreditScoringModule()
    local_scoring_service = LocalScoringService()

    def generate_score(self, data):
        print '--------------------'
        age_score = self.age_scoring_module.calculate_score(data)
        print 'Age score: %s' % age_score.total_score
        print '--------------------'
        placement_score = self.placement_scoring_module.calculate_score(data)
        print 'Placement score: %s' % placement_score.total_score
        print '--------------------'
        personal_score = self.personal_scoring_module.calculate_score(data)
        print 'Personal score: %s' % personal_score.total_score
        print '--------------------'
        assets_score = self.asset_scoring_module.calculate_score(data)
        print 'Assets score: %s' % assets_score.total_score
        print '--------------------'
        loan_score = self.loan_scoring_module.calculate_score(data)
        print 'Loan score: %s' % loan_score.total_score
        print '--------------------'
        # total_score = age_score.total_score + \
        #               placement_score.total_score + \
        #               personal_score.total_score + \
        #               assets_score.total_score + \
        #               loan_score.total_score
        total_score = self._calculate_total_score(age_score)
        total_rating = self.calculate_rating(total_score)
        print 'Total score: %s' % total_score
        print 'Total rating: "%s"' % total_rating
        print '--------------------'
        data = LocalScoringPlainModel(
            age_score=age_score,
            placement_score=placement_score,
            personal_score=personal_score,
            assets_score=assets_score,
            loan_score=loan_score,
            total_score=total_score,
            rating=total_rating,
        )
        local_scoring_data = self.local_scoring_service.create(data)
        return local_scoring_data

    def calculate_rating(self, total_score):
        rating = 'G'
        for item in sorted(self.main_local_scoring_card.get_card(),
                           key=lambda key: self.main_local_scoring_card.get_card()[key]):
            if total_score >= self.main_local_scoring_card.max_score:
                rating = self.main_local_scoring_card.max_rate
            if total_score < int(self.main_local_scoring_card.get_card()[item]):
                rating = item
                break
        return rating

    def _calculate_total_score(self, age_data, placement_data, personal_data, loan_data):
        main = self._calculate_main_parameters(age_data, placement_data)
        personal = self._calculate_personal_parameters(personal_data)
        placement = self._calculate_placement_parameters(placement_data)
        loan = self._calculate_debts_parameters(loan_data)
        total = main + personal + placement + loan
        return total

    def _calculate_main_parameters(self, age_data, placement_data):
        score = (age_data.total_score + placement_data.placement_type_score.placement_type_score +
                 placement_data.placement_clean_income.placement_clean_income +
                 placement_data.placement_income_score.placement_income_score)/4 * 0.65
        return score

    def _calculate_personal_parameters(self, personal_data):
        score = (personal_data.education_score + personal_data.marital_status_score +
                 personal_data.official_address_score + personal_data.real_address_score +
                 personal_data.identity_addresses_score)/5 * 0.05
        return score

    def _calculate_placement_parameters(self, placement_data):
        category = placement_data.placement_income_score.category_position_score if \
            placement_data.placement_income_score.category_position_score else 0
        count = placement_data.placement_income_score.count_employees_score if \
            placement_data.placement_income_score.count_employees_score else 0
        tax = placement_data.placement_income_score.tax_score if placement_data.placement_income_score.tax_score else 0
        score = (placement_data.work_score.term_score +
                 placement_data.placement_income_score.placement_income_score + category + count + tax)
        return score

    def _calculate_debts_parameters(self, loan_data):
        if loan_data.outstanding_loan_score == self.loan_scoring_module.outstanding_loans_actions.get_max_score():
            score = (loan_data.outstanding_loan_score + loan_data.dependents_score)/2 * 0.15
        else:
            score = (loan_data.outstanding_loan_score + loan_data.dependents_score + loan_data.amount_loan_score +
                     loan_data.repayment_percent_score + loan_data.days_to_repayment_score +
                     loan_data.monthly_payment_score + loan_data.debt_burden_score)/7 * 0.15
        return score