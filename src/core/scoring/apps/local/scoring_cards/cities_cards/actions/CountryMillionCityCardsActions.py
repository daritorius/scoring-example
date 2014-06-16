# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from django.utils.translation import ugettext as _


class CountryMillionCityCardsActions(BaseScoringCardActions):

    def get_millions_city_by_country(self, country_code):
        return self._navigate_card(country_code)

    def _navigate_card(self, country_code):
        cities = {
            'ua': self.__get_ua_cities(),
        }
        return cities[country_code]

    def __get_ua_cities(self):
        return [u'kiev', u'odessa', u'kharkov', u'киев', u'одесса', u'харьков']