# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.personal_cards.models import LocalPersonalMaritalStatusNormalCard
from django.utils.translation import ugettext as _


class LocalMaritalStatusNormalCardService(BaseService):
    model_instance = LocalPersonalMaritalStatusNormalCard