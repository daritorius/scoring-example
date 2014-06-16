# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.assets_cards.models import LocalDepositAmountCard
from django.utils.translation import ugettext as _


class LocalDepositAmountCardService(BaseService):
    model_instance = LocalDepositAmountCard