# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.personal_cards.models import LocalPersonalEducationCard
from django.utils.translation import ugettext as _


class LocalPersonalEducationCardService(BaseService):
    model_instance = LocalPersonalEducationCard