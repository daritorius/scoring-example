# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _


class UserProfile(models.Model):

    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode('ID: %s | user: %s' % (self.pk, self.user.pk))

    class Meta:
        db_table = 'user_profile'
        verbose_name = _(u'Users profiles')
        verbose_name_plural = _(u'Users profiles')