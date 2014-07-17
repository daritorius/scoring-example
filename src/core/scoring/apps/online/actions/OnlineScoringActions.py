# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from core.scoring.apps.online.apps.geo.actions.GeoGoogleActions import GeoGoogleActions
from core.scoring.apps.online.apps.geo.actions.GeoYandexActions import GeoYandexActions
from core.scoring.apps.online.apps.geo.plain_models import GeoYandexPlainModel, GeoGooglePlainModel
from core.scoring.apps.online.apps.geo.services.GeoGoogleService import GeoGoogleService
from core.scoring.apps.online.apps.geo.services.GeoYandexService import GeoYandexService
from core.scoring.apps.online.apps.search_engines.actions.GoogleActions import SearchGoogleActions
from core.scoring.apps.online.apps.search_engines.actions.YandexActions import SearchYandexActions
from core.scoring.apps.online.plain_models import OnlineScoringItemsPlainModels
from core.scoring.apps.online.services.OnlineScoringItemsService import OnlineScoringItemsService
from django.utils.translation import ugettext_lazy as _


class OnlineScoringActions(BaseActions):
    geo_google_actions = GeoGoogleActions()
    geo_google_service = GeoGoogleService()
    geo_yandex_actions = GeoYandexActions()
    geo_yandex_service = GeoYandexService()
    search_google_actions = SearchGoogleActions()
    search_yandex_actions = SearchYandexActions()
    online_scoring_service = OnlineScoringItemsService()

    def calculate_online_scoring(self, data, local_scoring=None, start=False):
        if local_scoring:
            data = OnlineScoringItemsPlainModels(local_scoring=local_scoring)
            self.online_scoring_service.create(data)
        if start and data:
            ## check geo google
            geo_google = self._process_geo_google(data)
            data = GeoGooglePlainModel(data=geo_google, query=self.geo_google_actions.make_query(data))
            self.geo_google_service.create(data)
            data = GeoGooglePlainModel(data=geo_google,
                                       query=self.geo_google_actions.make_query(data, address_type='real'))
            self.geo_google_service.create(data)
            ## check geo yandex
            geo_yandex = self._process_geo_yandex(data)
            data = GeoYandexPlainModel(data=geo_yandex, query=self.geo_yandex_actions.make_query(data))
            self.geo_google_service.create(data)
            data = GeoYandexPlainModel(data=geo_yandex,
                                       query=self.geo_yandex_actions.make_query(data, address_type='real'))
            self.geo_google_service.create(data)

            self._process_search_google(data)
            self._process_search_yandex(data)

    def _process_geo_google(self, data):
        return self.geo_google_actions.check_address(data)

    def _process_geo_yandex(self, data):
        return self.geo_yandex_actions.check_address(data)

    def _process_search_google(self, data):
        pass

    def _process_search_yandex(self, data):
        return self.search_yandex_actions.check_personal_information(data)