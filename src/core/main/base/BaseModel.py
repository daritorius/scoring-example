# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext as _


class BaseModel(models.Model):
    date_create = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)
    date_update = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    is_deleted = models.BooleanField(default=False)