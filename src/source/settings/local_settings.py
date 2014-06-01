# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
import main_settings as settings
from datetime import timedelta
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
ASSETS_DEBUG = DEBUG

del settings, os, timedelta