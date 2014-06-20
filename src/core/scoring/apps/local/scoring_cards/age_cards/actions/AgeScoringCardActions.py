# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.age_cards.services.AgeScoringCardService import AgeScoringCardService
from django.utils.translation import ugettext as _


class AgeScoringCardActions(BaseScoringCardActions):
    service = AgeScoringCardService()
    year_correction = 1