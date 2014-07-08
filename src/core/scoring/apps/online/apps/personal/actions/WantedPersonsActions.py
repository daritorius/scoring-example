# -*- coding: utf-8 -*-
from core.main.base.actions.BaseOnlineScoringActions import BaseOnlineScoringActions
from django.utils.translation import ugettext_lazy as _


class WantedPersonsActions(BaseOnlineScoringActions):
    url = 'http://mvs.gov.ua/mvs/control/investigation/search/wantedPerson'