# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalPersonalEducationCardService import \
    LocalPersonalEducationCardService
from django.utils.translation import ugettext as _


class LocalPersonalEducationCardActions(BaseScoringCardActions):
    service = LocalPersonalEducationCardService()