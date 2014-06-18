# -*- coding: utf-8 -*-
from core.scoring.apps.local.scoring_cards.placement_cards.models import LocalPlacementTypeCard, \
    LocalPlacementIncomeCard, LocalPlacementCleanIncomeCard, LocalPlacementWageTermCard, \
    LocalPlacementWageEarnAmountCard, LocalPlacementWageCategoryCard, LocalPlacementPeTermCard, \
    LocalPlacementPeTaxCard, LocalPlacementPeEmployeesCard
from django.contrib import admin
from django.utils.translation import ugettext as _


admin.site.register(LocalPlacementTypeCard)
admin.site.register(LocalPlacementIncomeCard)
admin.site.register(LocalPlacementCleanIncomeCard)
admin.site.register(LocalPlacementWageTermCard)
admin.site.register(LocalPlacementWageEarnAmountCard)
admin.site.register(LocalPlacementWageCategoryCard)
admin.site.register(LocalPlacementPeTermCard)
admin.site.register(LocalPlacementPeTaxCard)
admin.site.register(LocalPlacementPeEmployeesCard)