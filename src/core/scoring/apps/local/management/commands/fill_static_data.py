# -*- coding: utf-8 -*-
from core.scoring.apps.country.services.CountryService import CountryService
from core.scoring.apps.local.plain_models import LocalStaticDataPlainModel
from core.scoring.apps.local.services.LocalStaticDataService import LocalStaticDataService
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):
    country_service = CountryService()
    static_data_service = LocalStaticDataService()

    data_region = {
        u'Киев': {
            'wage': 5382,
            'food': 2422,
            'health': 269,
            'clothes': 377,
            'utilities': 646,
            'rent_region_center': 3600,
            'rent_region_all': 0,
        },
        u'Черниговская область': {
            'wage': 2594,
            'food': 1167,
            'health': 130,
            'clothes': 182,
            'utilities': 311,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Черновицкая область': {
            'wage': 2448,
            'food': 1102,
            'health': 122,
            'clothes': 171,
            'utilities': 294,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Черкасская область': {
            'wage': 2695,
            'food': 1213,
            'health': 135,
            'clothes': 189,
            'utilities': 323,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Хмельницкая область': {
            'wage': 2733,
            'food': 1230,
            'health': 137,
            'clothes': 191,
            'utilities': 328,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Херсонская область': {
            'wage': 2477,
            'food': 1115,
            'health': 124,
            'clothes': 173,
            'utilities': 297,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Харьковская область': {
            'wage': 3028,
            'food': 1363,
            'health': 151,
            'clothes': 212,
            'utilities': 363,
            'rent_region_center': 3000,
            'rent_region_all': 1200,
        },
        u'Тернопольская область': {
            'wage': 2365,
            'food': 1064,
            'health': 118,
            'clothes': 166,
            'utilities': 284,
            'rent_region_center': 2100,
            'rent_region_all': 1080,
        },
        u'Сумская область': {
            'wage': 2744,
            'food': 1235,
            'health': 137,
            'clothes': 192,
            'utilities': 329,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Ровенская область': {
            'wage': 2877,
            'food': 1295,
            'health': 144,
            'clothes': 201,
            'utilities': 345,
            'rent_region_center': 1500,
            'rent_region_all': 900,
        },
        u'Полтавская область': {
            'wage': 3000,
            'food': 1350,
            'health': 150,
            'clothes': 210,
            'utilities': 360,
            'rent_region_center': 1500,
            'rent_region_all': 900,
        },
        u'Одесская область': {
            'wage': 3014,
            'food': 1356,
            'health': 151,
            'clothes': 211,
            'utilities': 362,
            'rent_region_center': 2100,
            'rent_region_all': 1080,
        },
        u'Николаевская область': {
            'wage': 3266,
            'food': 1470,
            'health': 163,
            'clothes': 229,
            'utilities': 392,
            'rent_region_center': 2100,
            'rent_region_all': 1080,
        },
        u'Львовская область': {
            'wage': 2846,
            'food': 1281,
            'health': 142,
            'clothes': 199,
            'utilities': 342,
            'rent_region_center': 2100,
            'rent_region_all': 1080,
        },
        u'Луганская область': {
            'wage': 3483,
            'food': 1567,
            'health': 174,
            'clothes': 244,
            'utilities': 418,
            'rent_region_center': 1500,
            'rent_region_all': 900,
        },
        u'Кировоградская область': {
            'wage': 2668,
            'food': 1201,
            'health': 133,
            'clothes': 187,
            'utilities': 320,
            'rent_region_center': 1500,
            'rent_region_all': 900,
        },
        u'Киевская область': {
            'wage': 3442,
            'food': 1549,
            'health': 172,
            'clothes': 241,
            'utilities': 413,
            'rent_region_center': 3000,
            'rent_region_all': 3000,
        },
        u'Ивано-Франковская область': {
            'wage': 2724,
            'food': 1226,
            'health': 136,
            'clothes': 191,
            'utilities': 327,
            'rent_region_center': 1500,
            'rent_region_all': 900,
        },
        u'Запорожская область': {
            'wage': 3318,
            'food': 1493,
            'health': 166,
            'clothes': 232,
            'utilities': 398,
            'rent_region_center': 3000,
            'rent_region_all': 1200,
        },
        u'Закарпатская область': {
            'wage': 2556,
            'food': 1150,
            'health': 128,
            'clothes': 179,
            'utilities': 307,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Житомирская область': {
            'wage': 2641,
            'food': 1188,
            'health': 132,
            'clothes': 185,
            'utilities': 317,
            'rent_region_center': 1500,
            'rent_region_all': 900,
        },
        u'Донецкая область': {
            'wage': 4074,
            'food': 1833,
            'health': 204,
            'clothes': 285,
            'utilities': 489,
            'rent_region_center': 3000,
            'rent_region_all': 1200,
        },
        u'Днепропетровская область': {
            'wage': 3586,
            'food': 1614,
            'health': 179,
            'clothes': 251,
            'utilities': 430,
            'rent_region_center': 3000,
            'rent_region_all': 1200,
        },
        u'Волынская область': {
            'wage': 2538,
            'food': 1142,
            'health': 127,
            'clothes': 178,
            'utilities': 305,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'Винницкая область': {
            'wage': 2672,
            'food': 1202,
            'health': 134,
            'clothes': 187,
            'utilities': 321,
            'rent_region_center': 1200,
            'rent_region_all': 600,
        },
        u'АР Крым': {
            'wage': 0,
            'food': 0,
            'health': 0,
            'clothes': 0,
            'utilities': 0,
            'rent_region_center': 0,
            'rent_region_all': 0,
        },
        u'Севастополь': {
            'wage': 0,
            'food': 0,
            'health': 0,
            'clothes': 0,
            'utilities': 0,
            'rent_region_center': 0,
            'rent_region_all': 0,
        },
    }

    def handle(self, *args, **options):
        for key, value in self.data_region.iteritems():
            data = LocalStaticDataPlainModel(
                country=self.country_service.get_item(title='ua'),
                region=key,
                wage=value['wage'],
                food=value['food'],
                health=value['health'],
                clothes=value['clothes'],
                utilities=value['utilities'],
                rent_region_center=value['rent_region_center'],
                rent_region_all=value['rent_region_all']
            )
            self.static_data_service.create(data)