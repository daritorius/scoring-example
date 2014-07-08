# -*- coding: utf-8 -*-
from core.scoring.apps.online.apps.geo.actions.YandexActions import YandexActions
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):
    yandex_actions = YandexActions()

    def handle(self, *args, **options):
        data = {}
        self.yandex_actions.check_address(data)