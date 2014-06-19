# -*- coding: utf-8 -*-
from core.main.base.actions.BaseActions import BaseActions
from core.scoring.apps.local.scoring_cards.cities_cards.services.ScoringCityMillionaireService import \
    ScoringCityMillionaireService
from django.utils.translation import ugettext_lazy as _


class ScoringCityMillionaireActions(BaseActions):
    service = ScoringCityMillionaireService()