# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.BaseScoringCards import BaseScoringCards
from django.utils.translation import ugettext as _


class CountryMillionCityCards(BaseScoringCards):

    def get_millions_city_by_country(self, country_code):
        return self._navigate_card(country_code)

    def _navigate_card(self, country_code):
        cities = {
            'ua': self.__get_ua_cities()
        }
        return cities[country_code]

    def __get_ua_cities(self):
        return ['kiev', 'odessa', 'kharkov', 'киев', 'одесса', 'харьков']