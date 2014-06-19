# -*- coding: utf-8 -*-
from core.main.base.scoring.cards.BaseScoringCards import BaseScoringCardActions
from core.scoring.apps.local.scoring_cards.personal_cards.services.LocalMaritalStatusNormalCardService import \
    LocalMaritalStatusNormalCardService
from django.utils.translation import ugettext as _


class LocalMaritalStatusNormalCardActions(BaseScoringCardActions):
    service = LocalMaritalStatusNormalCardService()