# -*- coding: utf-8 -*-
from core.main.base.BasePlainModel import BasePlainModel
from django.utils.translation import ugettext as _


class UserProfilePlainModel(BasePlainModel):
    fields = ['user']