# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.BaseScoringCards import BaseScoringCards
from django.utils.translation import ugettext as _


class PersonalInformationCards(BaseScoringCards):
    min_score = -300
    max_score = 300

    min_address_city_score = 0
    max_address_city_score = 300

    min_identity_address_score = 0
    max_identity_address_score = 300

    def get_education_card(self):
        """
            EDUCATION TYPES:
            HIGH_EDUCATION = 0
            MIDDLE_EDUCATION = 1
            MIDDLE_TECH_EDUCATION = 2
            NOT_FINISHED_HIGH_EDUCATION = 3
            TWO_OR_MORE_HIGH_EDUCATION = 4
            DEGREE_EDUCATION = 4
            NOT_FINISHED_MIDDLE_EDUCATION = 5
        """

        card = {
            '5': -300,
            '1': -200,
            '2': 100,
            '3': -100,
            '0': 200,
            '4': 300
        }
        return card

    def get_marital_status_card(self):
        """
            MARITAL STATUSES:
            FALSE_MARITAL_STATUS = 0
            TRUE_MARITAL_STATUS = 1
            WIDOW_MARITAL_STATUS = 2
            DIVORCED_MARITAL_STATUS = 3
        """

        card = {
            '1': 300,
            '0': -100,
            '3': -300,
            '2': 0
        }
        return card

    def get_identity_addresses_card(self):
        card = {
            'yes': 300,
            'no': 0
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