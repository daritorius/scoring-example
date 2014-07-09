# -*- coding: utf-8 -*-
from core.main.base.modules.Singleton import Singleton
from core.scoring.apps.online.apps.geo.actions.GoogleActions import GoogleActions
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Data(object):
    __metaclass__ = Singleton

    def __init__(self):
        setattr(self, 'profile_official_address', OfficialAddress())
        setattr(self, 'profile_real_address', RealAddress())


class OfficialAddress(object):
    __metaclass__ = Singleton

    def __init__(self):
        setattr(self, 'official_country', 'Украина')
        setattr(self, 'official_city', 'Киев')
        setattr(self, 'official_street', '1 мая')
        setattr(self, 'official_house', '19')


class RealAddress(object):
    __metaclass__ = Singleton

    def __init__(self):
        setattr(self, 'real_country', 'Украина')
        setattr(self, 'real_city', 'Киев')
        setattr(self, 'real_street', '1 мая')
        setattr(self, 'real_house', '19')


class Command(BaseCommand):
    google_actions = GoogleActions()

    @staticmethod
    def generate_data():
        data = Data()
        return data

    def handle(self, *args, **options):
        data = self.generate_data()
        self.google_actions.check_address(data)