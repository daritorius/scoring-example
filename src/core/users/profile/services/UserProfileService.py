# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from core.users.profile.models import UserProfile
from django.utils.translation import ugettext as _


class UserProfileService(BaseService):
    model_instance = UserProfile