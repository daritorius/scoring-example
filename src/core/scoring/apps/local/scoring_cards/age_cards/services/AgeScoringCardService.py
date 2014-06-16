# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.age_cards.models import LocalAgeScoringCard


class AgeScoringCardService(BaseService):
    model_instance = LocalAgeScoringCard