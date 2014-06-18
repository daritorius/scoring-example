# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

    def fill_age_cards(self):
        pass

    def fill_assets_cards(self):
        pass

    def fill_cities_cards(self):
        pass

    def fill_loan_cards(self):
        pass

    def fill_personal_cards(self):
        pass

    def fill_placement_cards(self):
        pass