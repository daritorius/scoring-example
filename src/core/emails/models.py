# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class EmailTemplate(models.Model):

    title = models.CharField(max_length=255, null=False, unique=True)
    subject = models.CharField(max_length=255, null=False)
    body = models.TextField(max_length=2048, blank=True, null=True)
    date_create = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)
    date_update = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'email_templates'
        verbose_name = _(u'templates for emails')
        verbose_name_plural = _(u'templates for emails')


class Email(models.Model):

    STATUS_UNDEFINED = 0
    STATUS_SENT = 1
    STATUS = (
        (STATUS_UNDEFINED, 'Undefined'),
        (STATUS_SENT, 'Sent')
    )

    subject = models.CharField(max_length=255, null=False)
    body = models.TextField(max_length=2048, blank=True, null=True)
    email_to = models.EmailField(max_length=255, null=False, db_index=True)
    status = models.IntegerField(choices=STATUS, default=STATUS_UNDEFINED)
    date_create = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)
    date_update = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s' % (self.email_to, self.subject)

    class Meta:
        db_table = 'emails'
        verbose_name = _(u'emails')
        verbose_name_plural = _(u'emails')