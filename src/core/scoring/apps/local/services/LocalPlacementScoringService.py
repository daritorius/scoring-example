# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.models import LocalPlacementScoring
from django.utils.translation import ugettext as _


class LocalPlacementScoringService(BaseService):
    model_instance = LocalPlacementScoring