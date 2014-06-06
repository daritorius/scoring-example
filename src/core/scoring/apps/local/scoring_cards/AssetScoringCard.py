# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.BaseScoringCards import BaseScoringCards
from django.utils.translation import ugettext_lazy as _


class AssetScoringCard(BaseScoringCards):

    # 'assets_available_assets',
    # 'assets_flat',
    # 'assets_flat_address',
    # 'assets_flat_area',
    # 'assets_flat_state',
    # 'assets_house',
    # 'assets_house_address',
    # 'assets_house_area',
    # 'assets_house_state',
    # 'assets_car',
    # 'assets_car_mark',
    # 'assets_car_model',
    # 'assets_car_year_manufacture',
    # 'assets_car_mileage',
    # 'assets_car_state',
    # 'assets_deposits',
    # 'assets_deposits_amount',
    # 'assets_deposits_monthly_percents',
    # 'assets_deposits_maturity_date',
    # 'assets_other_assets',
    # 'assets_other_assets_title',
    # 'assets_other_assets_price',

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