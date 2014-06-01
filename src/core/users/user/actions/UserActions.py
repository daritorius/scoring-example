# -*- coding: utf-8 -*-
from core.users.user.services.UserService import UserService
from django.utils.translation import ugettext as _


class UserActions(object):
    user_service = UserService()