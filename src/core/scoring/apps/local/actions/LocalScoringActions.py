# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from core.scoring.apps.local.actions.modules.AssetScoringModule import AssetScoringModule
from core.scoring.apps.local.actions.modules.CreditScoringModule import CreditScoringModule
from core.scoring.apps.local.plain_models import LocalScoringPlainModel
from core.scoring.apps.local.services.LocalScoringService import LocalScoringService
from core.scoring.scoring_cards.MainLocalScoringCard import MainLocalScoringCard
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
        total_score = self._calculate_total_score(age_score, placement_score, personal_score, loan_score)
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
        print 'main parameters score: %s' % main
        personal = self._calculate_personal_parameters(personal_data)
        print 'personal parameters score: %s' % personal
        placement = self._calculate_placement_parameters(placement_data)
        print 'placement parameters score: %s' % placement
        loan = self._calculate_debts_parameters(loan_data)
        print 'loan parameters score: %s' % loan
        total = int(round(main + personal + placement + loan, 0))
        return total

    @staticmethod
    def _calculate_main_parameters(age_data, placement_data):
        score = float((int(age_data.total_score) +
                       int(placement_data.placement_type_score) +
                       int(placement_data.placement_clean_income) +
                       int(placement_data.placement_income_score))) / 4 * 0.65
        return score

    @staticmethod
    def _calculate_personal_parameters(personal_data):
        score = float((int(personal_data.education_score) +
                       int(personal_data.marital_status_score) +
                       int(personal_data.official_address_score) +
                       int(personal_data.real_address_score) +
                       int(personal_data.identity_addresses_score))) / 5 * 0.05
        return score

    @staticmethod
    def _calculate_placement_parameters(placement_data):
        category = placement_data.category_position_score if \
            placement_data.category_position_score else 0
        count = placement_data.count_employees_score if \
            placement_data.count_employees_score else 0
        tax = placement_data.tax_score if placement_data.tax_score else 0
        score = 0
        if placement_data.placement_type_score == 300:
            score = float((int(placement_data.term_score) +
                           int(placement_data.wage_score) +
                           int(category))) / 4 * 0.15
        elif placement_data.placement_type_score == 200:
            score = float((int(placement_data.term_score) +
                           int(tax) +
                           int(count))) / 3 * 0.15
        return score

    def _calculate_debts_parameters(self, loan_data):
        if loan_data.outstanding_loan_score == self.loan_scoring_module.outstanding_loans_actions.get_max_score():
            score = float((int(loan_data.outstanding_loan_score) +
                           int(loan_data.dependents_score))) / 2 * 0.15
        else:
            score = float((int(loan_data.outstanding_loan_score) +
                           int(loan_data.dependents_score) +
                           int(loan_data.amount_loan_score) +
                           int(loan_data.repayment_percent_score) +
                           int(loan_data.days_to_repayment_score) +
                           int(loan_data.monthly_payment_score) +
                           int(loan_data.debt_burden_score))) / 7 * 0.15
        return score