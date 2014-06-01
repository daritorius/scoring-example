# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from .. import main_settings as settings

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
            # "PASSWORD": "secretpassword", # Optional
        }
    },
}

CACHE_SERVICES = True
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "session"