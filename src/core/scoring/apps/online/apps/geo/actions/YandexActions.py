# -*- coding: utf-8 -*-
from core.main.base.actions.BaseOnlineScoringActions import BaseOnlineScoringActions
from django.utils.translation import ugettext_lazy as _


class YandexActions(BaseOnlineScoringActions):
    url = 'http://geocode-maps.yandex.ru/1.x/'
    query = 'geocode'

    def check_address(self, data):
        pass

    def check_official_address(self, data):
        city = getattr(data.profile_official_address, 'official_city') if \
            hasattr(data.profile_official_address, 'official_city') else None

    def check_real_address(self, data):
        pass