# -*- coding: utf-8 -*-
from core.main.base.services.BaseService import BaseService
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class UserService(BaseService):
    model_instance = User

    def get_by_email(self, email):
        return self.get_item(force=True, email=email)

    def create(self, item_data):
        item = self.model_instance(**item_data.__dict__)
        item.set_password(item_data.password)
        item.save()
        return item

    def update_password(self, email, password):
        user = self.get_by_email(email)
        user.set_password(password)
        user.save()
        return user