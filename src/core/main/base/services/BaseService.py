# -*- coding: utf-8 -*-
from core.main.base.facades.BaseFacade import Singleton
from core.main.cache.services.CacheService import CacheService
from django.db.models import Model
from django.utils.functional import SimpleLazyObject
from django.conf import settings


class BaseService(object):
    __metaclass__ = Singleton

    model_instance = None
    cache_service = CacheService()
    allowed_cache_services = [
        'CountryService',
        'ScoringService',
        'LocalAgeScoreService',
        'LocalAssetsScoringService',
        'LocalLoanScoringService',
        'LocalPersonalScoringService',
        'LocalPlacementScoringService',
        'LocalScoringService',
    ]

    def get_by_id(self, obj_id):
        try:
            if self.__class__.__name__ in self.allowed_cache_services and settings.CACHE_SERVICES:
                item = self.cache_service.get_cache(u'%s-%s' % (self.__class__.__name__, obj_id))
                if not item:
                    item = self.model_instance.objects.get(id=obj_id)
                    self.cache_service.create_cache(u'%s-%s' % (self.__class__.__name__, obj_id), item)
            else:
                item = self.model_instance.objects.get(id=obj_id)
            return item
        except self.model_instance.DoesNotExist:
            return None

    def get_all(self, order_by=None):
        try:
            if self.__class__.__name__ in self.allowed_cache_services and settings.CACHE_SERVICES:
                name = u'%s_all' % self.__class__.__name__ if not order_by else \
                    u'%s_all_%s' % (self.__class__.__name__, order_by)

                items = self.cache_service.get_cache(name)
                if not items:
                    items = self.model_instance.objects.all()
                    if order_by and len(items):
                        items = items.order_by(order_by)
                    self.cache_service.create_list_cache(name, items)
            else:
                items = self.model_instance.objects.all()
                if order_by and len(items):
                    items = items.order_by(order_by)
            return items
        except Exception:
            return []

    def create(self, item_data):
        item = self.model_instance()
        for key, value in item_data.__dict__.items():
            setattr(item, key, value)
        item.save()

        if self.__class__.__name__ in self.allowed_cache_services and settings.CACHE_SERVICES:
            self.cache_service.create_cache(u'%s-%s' % (self.__class__.__name__, item.pk), item)
            self.cache_service.delete_pattern(u'%s_*' % self.__class__.__name__)
        return item

    def update(self, item_id, item_data):
        item = self.model_instance.objects.get(id=item_id)
        for key, value in item_data.__dict__.items():
            setattr(item, key, value)
        item.save()

        if self.__class__.__name__ in self.allowed_cache_services and settings.CACHE_SERVICES:
            self.cache_service.update_cache(u'%s-%s' % (self.__class__.__name__, item.pk), item)
            self.cache_service.delete_pattern(u'%s_*' % self.__class__.__name__)
        return item

    def delete(self, item_id):
        item = self.get_by_id(item_id)
        item.is_deleted = True
        item.save()

        if self.__class__.__name__ in self.allowed_cache_services:
            self.cache_service.delete_cache(u'%s-%s' % (self.__class__.__name__, item.pk))
            self.cache_service.delete_pattern(u'%s_*' % self.__class__.__name__)
        return item

    def select(self, cache=True, force=False, is_deleted=False, order_by=None, query=None, **kwargs):
        try:
            if self.__class__.__name__ in self.allowed_cache_services and cache and settings.CACHE_SERVICES:
                name = u'%s_is_de=%s_or_by=%s' % (self.__class__.__name__, is_deleted, order_by) if not force \
                    else u'%s_or_by=%s' % (self.__class__.__name__, order_by)
                for key, value in kwargs.items():
                    if isinstance(value, Model):
                        value = value.pk
                    elif isinstance(value, SimpleLazyObject):
                        value = value.pk
                    name += u'_%s=%s' % (str(key)[:5], value)
                if query:
                    name += u'%s' % str(query)
                name = u''.join(name.split()).replace(' ', '_')
                items = self.cache_service.get_cache(name)
                if not items:
                    if query:
                        items = self.model_instance.objects.filter(query, is_deleted=is_deleted, **kwargs) \
                            if not force else self.model_instance.objects.filter(query, **kwargs)
                    else:
                        items = self.model_instance.objects.filter(is_deleted=is_deleted, **kwargs) if not force \
                            else self.model_instance.objects.filter(**kwargs)
                    if order_by and len(items):
                        items = items.order_by(order_by)
                    self.cache_service.create_list_cache(name, items)
                for item in items:
                    if not self.cache_service.get_cache(u'%s-%s' % (self.__class__.__name__, item.pk)):
                        self.cache_service.create_cache(u'%s-%s' % (self.__class__.__name__, item.pk), item)
                        self.cache_service.delete_pattern(u'%s_*' % self.__class__.__name__)
            else:
                if query:
                    items = self.model_instance.objects.filter(query, is_deleted=is_deleted, **kwargs) if not force \
                        else self.model_instance.objects.filter(query, **kwargs)
                else:
                    items = self.model_instance.objects.filter(is_deleted=is_deleted, **kwargs) if not force \
                        else self.model_instance.objects.filter(**kwargs)
                if order_by and len(items):
                    items = items.order_by(order_by)
            return items
        except (UnicodeDecodeError, UnicodeEncodeError):
            if query:
                items = self.model_instance.objects.filter(query, is_deleted=is_deleted, **kwargs) if not force \
                    else self.model_instance.objects.filter(query, **kwargs)
            else:
                items = self.model_instance.objects.filter(is_deleted=is_deleted, **kwargs) if not force \
                    else self.model_instance.objects.filter(**kwargs)
            if order_by and len(items):
                items = items.order_by(order_by)
            return items

    def get_item(self, cache=True, force=False, is_deleted=False, query=None, **kwargs):
        try:
            if self.__class__.__name__ in self.allowed_cache_services and cache and settings.CACHE_SERVICES:
                name = u'%s_is_deleted=%s' % (self.__class__.__name__, is_deleted) if not force \
                    else u'%s' % self.__class__.__name__
                for key, value in kwargs.items():
                    if isinstance(value, Model):
                        value = value.pk
                    elif isinstance(value, SimpleLazyObject):
                        value = value.pk
                    name += u'_%s=%s' % (str(key), value)
                if query:
                    name += u'%s' % str(query)
                name = u''.join(name.split()).replace(' ', '_')
                item = self.cache_service.get_cache(name)
                if not item:
                    try:
                        if query:
                            item = self.model_instance.objects.get(query, is_deleted=is_deleted, **kwargs) \
                                if not force else self.model_instance.objects.get(query, **kwargs)
                        else:
                            item = self.model_instance.objects.get(is_deleted=is_deleted, **kwargs) if not force else \
                                self.model_instance.objects.get(**kwargs)
                        if not self.cache_service.get_cache(u'%s-%s' % (self.__class__.__name__, item.pk)):
                            self.cache_service.create_cache(u'%s-%s' % (self.__class__.__name__, item.pk), item)
                    except self.model_instance.DoesNotExist:
                        item = None
            else:
                try:
                    if query:
                        item = self.model_instance.objects.get(query, is_deleted=is_deleted, **kwargs) if not force \
                            else self.model_instance.objects.get(query, **kwargs)
                    else:
                        item = self.model_instance.objects.get(is_deleted=is_deleted, **kwargs) if not force else \
                            self.model_instance.objects.get(**kwargs)
                except self.model_instance.DoesNotExist:
                    item = None
            return item
        except (UnicodeDecodeError, UnicodeEncodeError):
            try:
                if query:
                    return self.model_instance.objects.get(query, is_deleted=is_deleted, **kwargs) if not force else \
                        self.model_instance.objects.get(query, **kwargs)
                else:
                    return self.model_instance.objects.get(is_deleted=is_deleted, **kwargs) if not force else \
                        self.model_instance.objects.get(**kwargs)
            except self.model_instance.DoesNotExist:
                return None