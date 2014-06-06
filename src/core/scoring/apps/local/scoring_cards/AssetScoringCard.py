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

    def get_available_assets_card(self):
        card = {
            'yes': 300,
            'no': -300,
        }
        return card