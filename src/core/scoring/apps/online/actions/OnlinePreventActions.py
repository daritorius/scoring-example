# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from core.scoring.apps.online.apps.personal.actions.MissedPersonsActions import MissedPersonsActions
from core.scoring.apps.online.apps.personal.actions.WantedPersonsActions import WantedPersonsActions
from django.utils.translation import ugettext_lazy as _


class OnlinePreventActions(BaseActions):
    missed_persons_actions = MissedPersonsActions()
    wanted_persons_actions = WantedPersonsActions()

    def check_person(self, data):
        return True if self._check_missed_person(data) or self._check_wanted_person(data) else False

    def _check_missed_person(self, data):
        return self.missed_persons_actions.check_person(data)

    def _check_wanted_person(self, data):
        return self.wanted_persons_actions.check_person(data)