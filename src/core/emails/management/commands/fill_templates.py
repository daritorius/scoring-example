# -*- coding: utf-8 -*-
import os
from core.emails.plain_models import EmailTemplatePlainModel
from core.emails.services.EmailService import EmailService
from core.emails.services.EmailTemplateService import EmailTemplateService
from django.core.management import BaseCommand
from django.utils.translation import ugettext as _

path_to_files = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates/'))

templates = {
    'restore_password': u'[MyBrains] Сброс пароля',
}


class Command(BaseCommand):
    email_service = EmailService()
    email_template_service = EmailTemplateService()

    def handle(self, *args, **options):
        self.generate_templates()

    def generate_templates(self):
        for title, value in templates.items():
            if not self.email_template_service.get_email_template_by_title(title):
                print 'Process new template with title: %s' % title
                with open('%s/%s' % (path_to_files, title)) as f:
                    content = f.read()
                template_data = EmailTemplatePlainModel(
                    title=u'%s' % title,
                    subject=value,
                    body=content
                )
                self.email_template_service.create(template_data)
            else:
                template = self.email_template_service.get_email_template_by_title(title)
                print 'Process update template with title: %s' % title
                with open('%s/%s' % (path_to_files, title)) as f:
                    content = f.read()
                template.title = u'%s' % title
                template.subject = value
                template.body = content
                template.save()