# -*- coding: utf-8 -*-
import datetime
from core.scoring.apps.local.actions.modules.BaseScoringModule import BaseScoringModule
from core.scoring.apps.local.plain_models import LocalLoanScoringPlainModel
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LoanOutstandingLoansCardActions import \
    LoanOutstandingLoansCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LocalAmountLoansCardActions import \
    LocalAmountLoansCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LocalDaysRepaymentLoansCardActions import \
    LocalDaysRepaymentLoansCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LocalDebtBurdenLoansCardActions import \
    LocalDebtBurdenLoansCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LocalDependentsCardActions import \
    LocalDependentsCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LocalMonthlyPaymentLoansCardActions import \
    LocalMonthlyPaymentLoansCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.actions.LocalPercentRepaymentLoansCardActions import \
    LocalPercentRepaymentLoansCardActions
from core.scoring.apps.local.scoring_cards.loan_cards.plain_models import LocalOutstandingLoansCardPlainModel, \
    LocalDependentsCardPlainModel
from core.scoring.apps.local.services.LocalLoanScoringService import LocalLoanScoringService
from django.utils.translation import ugettext_lazy as _
from source.settings.apps_settings import BASE_DATE_FORMAT


class CreditScoringModule(BaseScoringModule):
    loan_service = LocalLoanScoringService()
    outstanding_loans_actions = LoanOutstandingLoansCardActions()
    amount_actions = LocalAmountLoansCardActions()
    days_repayment_actions = LocalDaysRepaymentLoansCardActions()
    debt_burden_actions = LocalDebtBurdenLoansCardActions()
    dependents_actions = LocalDependentsCardActions()
    monthly_payment_actions = LocalMonthlyPaymentLoansCardActions()
    percent_repayment_actions = LocalPercentRepaymentLoansCardActions()

    def calculate_score(self, data):
        outstanding_loan_score = self._calculate_outstanding_credit_score(data)
        if outstanding_loan_score != self.outstanding_loans_actions.get_max_score():
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
        else:
            amount_loan_score = repayment_percent_score = days_to_repayment_score = \
                monthly_payment_score = debt_burden_score = dependents_score = 0
        total_score = outstanding_loan_score + amount_loan_score + repayment_percent_score + \
                      days_to_repayment_score + monthly_payment_score + debt_burden_score + dependents_score
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
        score = self.outstanding_loans_actions.get_min_score()
        if hasattr(data.profile_credit_charges, 'charges_outstanding_loans'):
            data = LocalOutstandingLoansCardPlainModel(
                key=int(getattr(data.profile_credit_charges, 'charges_outstanding_loans')))
            score = self.outstanding_loans_actions.service.get_item(**data.__dict__).value if \
                self.outstanding_loans_actions.service.get_item(**data.__dict__) else \
                self.outstanding_loans_actions.get_min_score()
        return score

    def _calculate_amount_credit_score(self, data):
        score = self.amount_actions.get_min_score()
        if hasattr(data.profile_credit_charges, 'charges_initial_amount'):
            amount = getattr(data.profile_credit_charges, 'charges_initial_amount')
            if amount >= float(self.amount_actions.get_max_key()):
                score = self.amount_actions.get_min_score()
            else:
                for item in self.amount_actions.get_card(reverse=True):
                    if amount < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_percent_repayment_score(self, data):
        score = self.percent_repayment_actions.get_min_score()
        if hasattr(data.profile_credit_charges, 'charges_initial_amount') and \
                hasattr(data.profile_credit_charges, 'charges_current_amount'):
            purpose_amount = float(getattr(data.profile_credit_charges, 'charges_initial_amount'))
            current_amount = float(getattr(data.profile_credit_charges, 'charges_current_amount'))
            try:
                repayment_percent = 100 - ((current_amount / purpose_amount) * 100)
            except ZeroDivisionError:
                repayment_percent = 0
            if repayment_percent >= float(self.percent_repayment_actions.get_max_key()):
                score = self.percent_repayment_actions.get_max_score()
            else:
                for item in self.percent_repayment_actions.get_card():
                    if repayment_percent < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_maturity_date_score(self, data):
        score = self.days_repayment_actions.get_min_score()
        if hasattr(data.profile_credit_charges, 'charges_maturity_date'):
            maturity_date = datetime.datetime.strptime(
                getattr(data.profile_credit_charges, 'charges_maturity_date'), BASE_DATE_FORMAT)
            current_date = datetime.datetime.now()
            days = abs(maturity_date - current_date).days
            if days >= self.days_repayment_actions.get_max_key():
                score = self.days_repayment_actions.get_min_score()
            else:
                for item in self.days_repayment_actions.get_card():
                    if days < item.key:
                        score = item.value
                        break
        return score

    def _calculate_monthly_payment_score(self, data):
        score = self.monthly_payment_actions.get_min_score()
        if hasattr(data.profile_credit_charges, 'charges_monthly_payment'):
            payment = float(getattr(data.profile_credit_charges, 'charges_monthly_payment'))
            if payment >= float(self.monthly_payment_actions.get_max_key()):
                score = self.monthly_payment_actions.get_min_score()
            else:
                for item in self.monthly_payment_actions.get_card(reverse=True):
                    if payment < item.key:
                        score = item.value
                        break
        return score

    def _calculate_debt_burden_score(self, data):
        score = self.debt_burden_actions.get_min_score()
        if hasattr(data.profile_credit_charges, 'charges_monthly_payment') and \
                hasattr(data.profile_placement_information, 'placement_income'):
            payment = float(getattr(data.profile_credit_charges, 'charges_monthly_payment'))
            income = float(getattr(data.profile_placement_information, 'placement_income'))
            try:
                debt_burden = round(float(payment / income), 2)
            except ZeroDivisionError:
                debt_burden = 1
            if debt_burden >= float(self.debt_burden_actions.get_max_key()):
                score = self.debt_burden_actions.get_min_score()
            else:
                for item in self.debt_burden_actions.get_card(reverse=True):
                    if debt_burden < float(item.key):
                        score = item.value
                        break
        return score

    def _calculate_dependents_score(self, data):
        score = 0
        if hasattr(data.profile_personal_information, 'personal_dependents'):
            data = LocalDependentsCardPlainModel(
                key=int(getattr(data.profile_personal_information, 'personal_dependents')))
            score = self.dependents_actions.service.get_item(**data.__dict__).value if \
                self.dependents_actions.service.get_item(**data.__dict__) else self.dependents_actions.get_min_score()
        return score