# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class MainLocalScoringCard(object):
    max_score = 300
    min_score = -300
    max_rate = 'A'
    min_rate = 'G'

    def get_card(self):
        card = {
            'A': 300,
            'B': 199,
            'C': 99,
            'D': 0,
            'E': -1,
            'F': -51,
            'G': -151,
        }
        return card