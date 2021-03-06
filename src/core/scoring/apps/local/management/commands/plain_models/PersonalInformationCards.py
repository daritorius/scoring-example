# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class PersonalInformationCards(object):
    min_score = -300
    max_score = 300

    min_address_city_score = 0
    max_address_city_score = 300

    min_identity_address_score = 0
    max_identity_address_score = 300

    min_normal_marital_age = 30
    max_normal_marital_age = 65

    HIGH_EDUCATION = 0
    MIDDLE_EDUCATION = 1
    MIDDLE_TECH_EDUCATION = 2
    NOT_FINISHED_HIGH_EDUCATION = 3
    TWO_OR_MORE_HIGH_EDUCATION = 4
    DEGREE_EDUCATION = 4
    NOT_FINISHED_MIDDLE_EDUCATION = 5

    EDUCATION_TYPES = {
        str(HIGH_EDUCATION): u'Высшее',
        str(MIDDLE_EDUCATION): u'Среднее',
        str(MIDDLE_TECH_EDUCATION): u'Серднее техническое',
        str(NOT_FINISHED_HIGH_EDUCATION): u'Неоконченное высшее',
        str(TWO_OR_MORE_HIGH_EDUCATION): u'2 и более высших образования',
        str(DEGREE_EDUCATION): u'Ученая степень',
        str(NOT_FINISHED_MIDDLE_EDUCATION): u'Неоконченное среднее образование',
    }

    FALSE_MARITAL_STATUS = 0
    TRUE_MARITAL_STATUS = 1
    WIDOW_MARITAL_STATUS = 2
    DIVORCED_MARITAL_STATUS = 3

    MARITAL_STATUSES = {
        str(FALSE_MARITAL_STATUS): u'Незамужем/Неженат',
        str(TRUE_MARITAL_STATUS): u'Замужем/Женат',
        str(WIDOW_MARITAL_STATUS): u'Вдова/Вдовец',
        str(DIVORCED_MARITAL_STATUS): u'Разведена/Разведен',
    }

    def get_education_card(self):
        card = {
            '5': -300,
            '1': -200,
            '2': 100,
            '3': -100,
            '0': 200,
            '4': 300
        }
        return card

    def get_marital_status_normal_card(self):
        card = {
            '1': 300,
            '0': -100,
            '3': -300,
            '2': 0
        }
        return card

    def get_marital_status_bad_card(self):
        card = {
            '1': 300,
            '0': 0,
            '3': -300,
            '2': 0
        }
        return card

    def get_identity_addresses_card(self):
        card = {
            '1': 300,
            '0': 0
        }
        return card