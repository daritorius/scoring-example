# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


class CreditScoringCard(object):
    min_credit_score = 0
    max_credit_amount = 200000
    max_repayment_percent = 50
    max_maturity_days = 180
    max_monthly_payment = 6000
    max_debt_burden = 0.7

    def get_current_credit_card(self):
        card = {
            '1': -300,
            '0': 300,
        }
        return card

    def get_credit_amount_card(self):
        card = {
            '10000': 0,
            '50000': -100,
            '200000': -200,
            '200001': -300,
        }
        return card

    def get_percent_repayment_card(self):
        card = {
            '10': -300,
            '30': -200,
            '50': -100,
            '51': 0,
        }
        return card

    def get_days_to_repayment_card(self):
        card = {
            '30': -300,
            '90': -200,
            '180': -100,
            '181': 0,
        }
        return card

    def get_amount_monthly_payment_card(self):
        card = {
            '1000': 0,
            '2000': -100,
            '3000': -200,
            '6000': -300,
            '6001': -9999,
        }
        return card

    def get_debt_burden_card(self):
        card = {
            '0.5': 0,
            '0.55': -100,
            '0.6': -200,
            '0.7': -300,
            '0.71': -9999,
        }
        return card

    def get_count_dependents_card(self):

        """
            NO_DEPENDENTS = 0
            ONE_DEPENDENT = 1
            TWO_DEPENDENTS = 2
            THREE_DEPENDENTS = 3
            FOUR_DEPENDENTS = 4
            MORE_THAN_4_DEPENDENTS = 5
        """

        card = {
            '0': 300,
            '1': 0,
            '2': -100,
            '3': -200,
            '4': -300,
            '5': -300,
        }
        return card