# -*- coding: utf-8 -*-
from core.main.base.modules.Singleton import Singleton
from core.scoring.apps.online.apps.personal.actions.WantedPersonsActions import WantedPersonsActions
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
    wanted_actions = WantedPersonsActions()

    def handle(self, *args, **options):
        data = Data()
        self.wanted_actions.check_person(data)