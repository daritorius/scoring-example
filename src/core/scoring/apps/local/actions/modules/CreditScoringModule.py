# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.plain_models import LocalLoanScoringPlainModel
from core.scoring.apps.local.scoring_cards.CreditScoringCard import CreditScoringCard
from core.scoring.apps.local.services.LocalLoanScoringService import LocalLoanScoringService
from django.utils.translation import ugettext_lazy as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class CreditScoringModule(BaseScoringModule):
    cards = CreditScoringCard()
    loan_service = LocalLoanScoringService()

    def calculate_score(self, data):
        outstanding_loan_score = self._calculate_outstanding_credit_score(data)
        print 'outstatnding loan score: %s' % outstanding_loan_score
        amount_loan_score = self._calculate_amount_credit_score(data)
        print 'amount loan score: %s' % amount_loan_score
        repayment_percent_score = self._calculate_percent_repayment_score(data)
        print 'repayment percent score: %s' % repayment_percent_score
        days_to_repayment_score = self._calculate_maturity_date_score(data)
        print 'days to repayment score: %s' % days_to_repayment_score
        monthly_payment_score = self._calculate_monthly_payment_score(data)
        print 'monthly payment score: %s' % monthly_payment_score
        debt_burden_score = self._calculate_debt_burden_score(data)
        print 'debt burden score: %s' % debt_burden_score
        dependents_score = self._calculate_dependents_score(data)
        print 'dependents score: %s' % dependents_score
        total_score = outstanding_loan_score + \
                      amount_loan_score + \
                      repayment_percent_score + \
                      days_to_repayment_score + \
                      monthly_payment_score + \
                      debt_burden_score
        data = LocalLoanScoringPlainModel(
            outstanding_loan_score=outstanding_loan_score,
            amount_loan_score=amount_loan_score,
            repayment_percent_score=repayment_percent_score,
            days_to_repayment_score=days_to_repayment_score,
            monthly_payment_score=monthly_payment_score,
            debt_burden_score=debt_burden_score,
            dependents_score=dependents_score,
            total_score=total_score,
        )
        loan_data = self.loan_service.create(data)
        return loan_data

    def _calculate_outstanding_credit_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_credit_charges, 'charges_outstanding_loans'):
            score = self.cards.get_current_credit_card()[getattr(data.profile_credit_charges,
                                                                 'charges_outstanding_loans')[0]]
        return score

    def _calculate_amount_credit_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_credit_charges, 'charges_initial_amount'):
            amount = int(float(getattr(data.profile_credit_charges, 'charges_initial_amount')[0]))
            if amount >= self.cards.max_credit_amount:
                score = self.cards.min_score
            else:
                for item in sorted(self.cards.get_credit_amount_card(),
                                   key=lambda key: self.cards.get_credit_amount_card()[key], reverse=True):
                    if amount < int(item):
                        score = self.cards.get_credit_amount_card()[item]
                        break
        return score

    def _calculate_percent_repayment_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_credit_charges, 'charges_initial_amount') and \
                hasattr(data.profile_credit_charges, 'charges_current_amount'):
            purpose_amount = float(getattr(data.profile_credit_charges, 'charges_initial_amount')[0])
            current_amount = float(getattr(data.profile_credit_charges, 'charges_current_amount')[0])
            repayment_percent = 100 - ((current_amount / purpose_amount) * 100)
            if repayment_percent >= self.cards.max_repayment_percent:
                score = self.cards.max_score
            else:
                for item in sorted(self.cards.get_percent_repayment_card(),
                                   key=lambda key: self.cards.get_percent_repayment_card()[key]):
                    if repayment_percent < float(item):
                        score = self.cards.get_percent_repayment_card()[item]
                        break
        return score

    def _calculate_maturity_date_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_credit_charges, 'charges_maturity_date'):
            maturity_date = datetime.datetime.strptime(
                getattr(data.profile_credit_charges, 'charges_maturity_date')[0], BASE_DATE_FORMAT)
            current_date = datetime.datetime.now()
            days = abs(maturity_date - current_date).days
            if days >= self.cards.max_maturity_days:
                score = self.cards.min_credit_score
            else:
                for item in sorted(self.cards.get_days_to_repayment_card(),
                                   key=lambda key: self.cards.get_days_to_repayment_card()[key]):
                    if int(days) < int(item):
                        score = self.cards.get_days_to_repayment_card()[item]
                        break
        return score

    def _calculate_monthly_payment_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_credit_charges, 'charges_monthly_payment'):
            payment = int(float(getattr(data.profile_credit_charges, 'charges_monthly_payment')[0]))
            if payment >= self.cards.max_monthly_payment:
                score = self.cards.min_score
            else:
                for item in sorted(self.cards.get_amount_monthly_payment_card(),
                                   key=lambda key: self.cards.get_amount_monthly_payment_card()[key], reverse=True):
                    if payment < int(item):
                        score = self.cards.get_amount_monthly_payment_card()[item]
                        break
        return score

    def _calculate_debt_burden_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_credit_charges, 'charges_monthly_payment') and \
                hasattr(data.profile_placement_information, 'placement_income'):
            payment = float(getattr(data.profile_credit_charges, 'charges_monthly_payment')[0])
            income = float(getattr(data.profile_placement_information, 'placement_income')[0])
            debt_burden = payment / income
            if debt_burden >= self.cards.max_debt_burden:
                score = self.cards.min_score
            else:
                for item in sorted(self.cards.get_debt_burden_card(),
                                   key=lambda key: self.cards.get_debt_burden_card()[key], reverse=True):
                    if debt_burden < float(item):
                        score = self.cards.get_debt_burden_card()[item]
                        break
        return score

    def _calculate_dependents_score(self, data):
        score = self.cards.min_score
        if hasattr(data.profile_personal_information, 'personal_dependents'):
            score = self.cards.get_count_dependents_card()[getattr(
                data.profile_personal_information, 'personal_dependents')[0]]
        return score