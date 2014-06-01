# -*- coding: utf-8 -*-
from core.emails.models import Email
from core.emails.services.EmailService import EmailService
from django.core.mail import EmailMessage
from django.utils.translation import ugettext as _
from celery import current_app
from src.settings.apps_settings import DEFAULT_FROM_EMAIL


@current_app.task
def send_emails():
    try:
        emails = Email.objects.filter(status=Email.STATUS_UNDEFINED)
        for email in emails:
            from_email = DEFAULT_FROM_EMAIL
            msg = EmailMessage(email.subject, email.body, from_email, [email.email_to])
            msg.content_subtype = "html"
            msg.send()
            email.status = Email.STATUS_SENT
            email.save()
            print 'email sent to [%s]' % email.email_to
    except Exception as e:
        print e