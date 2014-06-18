# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class PlacementInformationCards(object):

    TYPE_UNEMPLOYED = 0
    TYPE_HOUSEWIFE = 1
    TYPE_STUDENT = 2
    TYPE_PENSIONER = 3
    TYPE_SOLDIER = 4
    TYPE_WAGE_EARNER = 5
    TYPE_PRIVATE_ENTREPRENEUR = 6

    PLACEMENT_TYPES = {
        str(TYPE_UNEMPLOYED): u'Безработный',
        str(TYPE_HOUSEWIFE): u'Домохозяйка',
        str(TYPE_STUDENT): u'Студент',
        str(TYPE_PENSIONER): u'Пенсионер',
        str(TYPE_SOLDIER): u'Военнослужащий',
        str(TYPE_WAGE_EARNER): u'Служащий',
        str(TYPE_PRIVATE_ENTREPRENEUR): u'Частный предприниматель',
    }

    min_type_score = -100
    min_income_score = -300
    max_income_score = 300
    max_income_amount = 80000.0
    min_clean_income_score = -300
    max_clean_income_score = -300
    max_clean_income_amount = 10000.0
    max_employ_score = 300
    min_employ_score = -300
    max_employ_term = 60
    min_employ_term = 12
    max_wage_amount = 44001
    min_wage_amount = 1200
    max_pe_tax_amount = 20000
    max_pe_employees_count = 10

    CATEGORY_SENIOR_MANAGER = 0
    CATEGORY_MIDDLE_MANAGER = 1
    CATEGORY_SPECIALIST = 2
    CATEGORY_JUNIOR_SPECIALIST = 3

    POSITION_CATEGORIES = {
        str(CATEGORY_SENIOR_MANAGER): u'Senior Manager',
        str(CATEGORY_MIDDLE_MANAGER): u'Middle Manager',
        str(CATEGORY_SPECIALIST): u'Specialist',
        str(CATEGORY_JUNIOR_SPECIALIST): u'Junior Specialist',
    }

    def get_placement_type_card(self):
        card = {
            '0': -300,
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

    def get_wage_earner_term_card(self):
        card = {
            '12': -300,
            '35': 100,
            '59': 200,
            '60': 300
        }
        return card

    def get_wage_earner_amount_card(self):
        card = {
            '1200': -300,
            '1600': -300,
            '1800': -280,
            '2000': -270,
            '2200': -260,
            '2400': -249,
            '2600': -250,
            '2800': -225,
            '3000': -200,
            '3200': -175,
            '3400': -149,
            '3600': -150,
            '3800': -125,
            '4000': -100,
            '4200': -75,
            '4400': -49,
            '4600': -50,
            '4800': -25,
            '5000': 0,
            '5500': 25,
            '6000': 50,
            '8000': 51,
            '10000': 75,
            '13000': 100,
            '16000': 125,
            '19000': 150,
            '22000': 151,
            '25000': 175,
            '28000': 200,
            '31000': 225,
            '33000': 250,
            '35000': 251,
            '38000': 270,
            '41000': 280,
            '44000': 290,
            '44001': 300,
        }
        return card

    def get_wage_earner_category_postition_card(self):
        """
            CATEGORY_SENIOR_MANAGER = 0
            CATEGORY_MIDDLE_MANAGER = 1
            CATEGORY_SPECIALIST = 2
            CATEGORY_JUNIOR_SPECIALIST = 3
        """
        card = {
            '0': 200,
            '1': 300,
            '2': 100,
            '3': -300,
        }
        return card

    def get_pe_term_card(self):
        card = {
            '12': -300,
            '59': 100,
            '60': 300
        }
        return card

    def get_pe_tax_card(self):
        card = {
            '1000': -300,
            '10000': 100,
            '20000': 200,
            '20001': 300,
        }
        return card

    def get_pe_count_employments_card(self):
        card = {
            '0': -300,
            '3': 0,
            '5': 100,
            '10': 200,
            '11': 300,
        }
        return card