# -*- coding: utf-8 -*-
from core.main.base.BasePlainModel import BasePlainModel
from django.utils.translation import ugettext as _


class UserPlainModel(BasePlainModel):
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'password']