# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.scoring_cards.personal_cards.models import LocalIdentityAddressesCard
from django.utils.translation import ugettext as _


class LocalIdentityAddressesCardService(BaseService):
    model_instance = LocalIdentityAddressesCard