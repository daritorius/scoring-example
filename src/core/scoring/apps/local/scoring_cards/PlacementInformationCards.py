# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.BaseScoringCards import BaseScoringCards
from django.utils.translation import ugettext as _


class PlacementInformationCards(BaseScoringCards):

    min_type_score = -100
    min_income_score = -300
    max_income_score = 300
    max_income_amount = 80000.0
    min_clean_income_score = -300
    max_clean_income_score = -300
    max_clean_income_amount = 10000.0
    max_employ_score = 300
    min_employ_score = -300

    def get_placement_type_card(self):
        """
            PLACEMENT_TYPE:

            TYPE_UNEMPLOYED = 0
            TYPE_HOUSEWIFE = 1
            TYPE_STUDENT = 2
            TYPE_PENSIONER = 3
            TYPE_SOLDIER = 4
            TYPE_WAGE_EARNER = 5
            TYPE_PRIVATE_ENTREPRENEUR = 6
        """
        card = {
            '0': 0,
            '1': -100,
            '2': -100,
            '3': 100,
            '4': 0,
            '5': 300,
            '6': 200,
        }
        return card

    def get_placement_income_card(self):
        card = {
            '1600.0': -300,
            '2000.0': -280,
            '2400.0': -270,
            '2800.0': -260,
            '3200.0': -249,
            '3600.0': -250,
            '4000.0': -225,
            '4200.0': -200,
            '4400.0': -175,
            '4600.0': -149,
            '4800.0': -150,
            '5000.0': -125,
            '5200.0': -100,
            '5400.0': -75,
            '5600.0': -49,
            '6000.0': -50,
            '6400.0': -25,
            '7000.0': 0,
            '7500.0': 25,
            '8000.0': 50,
            '12000.0': 51,
            '16000.0': 75,
            '20000.0': 100,
            '25000.0': 125,
            '30000.0': 150,
            '35000.0': 151,
            '40000.0': 175,
            '45000.0': 200,
            '50000.0': 225,
            '55000.0': 250,
            '60000.0': 251,
            '65000.0': 270,
            '70000.0': 280,
            '80000.0': 290
        }
        return card

    def get_placement_clean_income_card(self):
        card = {
            '200': -300,
            '400': -280,
            '600': -270,
            '800': -260,
            '1000': -249,
            '1200': -250,
            '1400': -225,
            '1600': -200,
            '1800': -175,
            '2000': -149,
            '2200': -150,
            '2400': -125,
            '2600': -100,
            '2800': -75,
            '3000': -49,
            '3200': -50,
            '3400': -25,
            '3600': 0,
            '3800': 25,
            '4000': 50,
            '4200': 51,
            '4400': 75,
            '4600': 100,
            '4800': 125,
            '5000': 150,
            '5200': 151,
            '5400': 175,
            '5600': 200,
            '5800': 225,
            '6000': 250,
            '7000': 251,
            '8000': 270,
            '9000': 280,
            '10000': 290,
        }
        return card