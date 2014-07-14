# -*- coding: utf-8 -*-
from core.main.base.modules.Singleton import Singleton
from core.scoring.apps.online.apps.search_engines.actions.YandexActions import YandexActions
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Data(object):
    __metaclass__ = Singleton

    def __init__(self):
        setattr(self, 'profile_first_name', 'Иван')
        setattr(self, 'profile_second_name', 'Иванович')
        setattr(self, 'profile_third_name', 'Иванов')
        setattr(self, 'profile_birthday', '17-09-1986')


class Command(BaseCommand):
    actions = YandexActions()

    def handle(self, *args, **options):
        data = Data()
        self.actions.check_simple_search(data)