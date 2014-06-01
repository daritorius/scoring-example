# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scoring',
        'USER': 'lendingstar',
        'PASSWORD': '_scoring_',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}