# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.cities_cards.models import ScoringCityMillionaire
from django.utils.translation import ugettext_lazy as _


class ScoringCityMillionaireService(BaseService):
    model_instance = ScoringCityMillionaire