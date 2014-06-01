#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.core.mail import EmailMessage
from django.core.management import BaseCommand
from core.emails.models import Email
from core.emails.services.EmailService import EmailService
from src.settings.apps_settings import DEFAULT_FROM_EMAIL


class Command(BaseCommand):
    email_service = EmailService()

    def handle(self, *args, **options):
        try:
            emails = Email.objects.filter(status=Email.STATUS_UNDEFINED)
            for email in emails:
                from_email = DEFAULT_FROM_EMAIL

                msg = EmailMessage(email.subject, email.body, from_email, [email.email_to])
                msg.content_subtype = "html"
                msg.send()

                print 'all emails sent'
        except Exception, e:
            import traceback
            print "%r\n%r" % (e, traceback.format_exc(),)
            print '-------------'
            print '\n'
            print e