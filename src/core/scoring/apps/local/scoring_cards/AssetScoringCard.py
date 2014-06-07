# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.BaseScoringCards import BaseScoringCards
from django.utils.translation import ugettext_lazy as _


class AssetScoringCard(BaseScoringCards):
    min_assets_score = 0
    max_flat_area = 120
    max_house_area = 300
    max_car_lifetime_years = 10
    max_car_mileage = 100000
    max_deposit_amount = 10000
    max_deposit_monthly_percents = 2000
    max_deposit_maturity_months = 13
    max_other_assets_price = 10000

    """
        REPAIR_STATE = 0
        NORMAL_STATE = 1
        GOOD_STATE = 2
        BEST_STATE = 3
    """

    def get_available_assets_card(self):
        card = {
            'yes': 300,
            'no': -300,
        }
        return card

    def get_flat_area_card(self):
        card = {
            '30': 0,
            '80': 100,
            '120': 200,
            '121': 300,
        }
        return card

    def get_assets_status_card(self):
        card = {
            '0': 0,
            '1': 100,
            '2': 200,
            '3': 300,
        }
        return card

    def get_house_area_card(self):
        card = {
            '50': 0,
            '150': 100,
            '300': 200,
            '301': 300,
        }
        return card

    def get_car_lifetime_card(self):
        card = {
            '1': 300,
            '5': 200,
            '10': 100,
            '11': 0,
        }
        return card

    def get_car_mileage_card(self):
        card = {
            '10000': 300,
            '50000': 200,
            '100000': 100,
            '100001': 0,
        }
        return card

    def get_deposit_maturity_date_card(self):
        card = {
            '2': 0,
            '6': 100,
            '12': 200,
            '13': 300,
        }
        return card

    def get_deposit_amount_card(self):
        card = {
            '1000': 0,
            '5000': 100,
            '10000': 200,
            '10001': 300,
        }
        return card

    def get_deposit_monthly_percents_card(self):
        card = {
            '0': 0,
            '500': 100,
            '2000': 200,
            '2001': 300,
        }
        return card

    def get_other_assets_price_card(self):
        card = {
            '1000': 0,
            '5000': 100,
            '10000': 200,
            '10001': 300,
        }
        return card