# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):

    def handle(self, *args, **options):
        # if isinstance(value, unicode):
        #     value = value.encode('utf8')
        # elif isinstance(value, str):
        #     value = value.decode('utf8')
        pass