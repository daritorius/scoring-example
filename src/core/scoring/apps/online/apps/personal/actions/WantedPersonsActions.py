# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from core.scoring.apps.online.apps.personal.actions.BasePersonsActions import BasePersonsActions


class WantedPersonsActions(BasePersonsActions):
    url = 'http://mvs.gov.ua/mvs/control/investigation/searchresults/wantedPerson'