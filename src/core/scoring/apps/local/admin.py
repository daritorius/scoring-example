# -*- coding: utf-8 -*-
from core.scoring.apps.local.models import LocalScoring, LocalAgeScore, LocalPlacementScoring, LocalPersonalScoring, \
    LocalAssetsScoring, LocalLoanScoring
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


admin.site.register(LocalScoring)
admin.site.register(LocalAgeScore)
admin.site.register(LocalPlacementScoring)
admin.site.register(LocalPersonalScoring)
admin.site.register(LocalAssetsScoring)
admin.site.register(LocalLoanScoring)