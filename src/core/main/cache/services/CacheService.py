# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.core.cache import get_cache


class CacheService(object):
    backend = 'default'
    cache_backend = get_cache(backend)
    default_time = None

    def clean_name(self, name):
        return str(name).replace(' ', '').replace('\n', '')[:249]

    def get_service_name(self, name):
        return name.split('_')[0]

    def create_list_cache(self, name, items, time=default_time):
        if not self.get_cache(name):
            self.cache_backend.set(self.clean_name(name), items, time)

    def create_cache(self, name, item, time=default_time):
        if not self.get_cache(self.clean_name(name)):
            self.cache_backend.set(self.clean_name(name), item, time)

    def get_cache(self, name):
        item = self.cache_backend.get(self.clean_name(name))
        return item

    def total_cache_clear(self):
        if self.backend == 'memcache':
            self.cache_backend.clear()

    def delete_cache(self, name):
        if self.backend == 'memcache':
            self.cache_backend.delete(self.clean_name(name))
        else:
            self.cache_backend.delete_pattern(self.clean_name(name))

    def delete_pattern(self, name):
        if self.backend == 'redis':
            self.cache_backend.delete_pattern(name)

    def update_cache(self, name, item):
        if not self.get_cache(self.clean_name(name)):
            self.create_cache(self.clean_name(name), item, self.default_time)
        else:
            self.delete_cache(self.clean_name(name))
            self.create_cache(self.clean_name(name), item, self.default_time)