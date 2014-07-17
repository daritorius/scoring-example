# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.online.models import OnlineScoringItems
from django.utils.translation import ugettext_lazy as _


class OnlineScoringItemsService(BaseService):
    model_instance = OnlineScoringItems