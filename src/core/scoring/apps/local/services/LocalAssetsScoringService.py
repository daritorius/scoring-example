# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.scoring.apps.local.models import LocalAssetsScoring
from django.utils.translation import ugettext as _


class LocalAssetsScoringService(BaseService):
    model_instance = LocalAssetsScoring