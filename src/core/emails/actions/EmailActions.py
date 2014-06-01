from django.core.mail import EmailMessage
from core.emails.models import Email
from core.emails.services.EmailService import EmailService
from src.settings.apps_settings import DEFAULT_FROM_EMAIL

email_service = EmailService()


class EmailActions(object):
    from_email = DEFAULT_FROM_EMAIL

    def send_email(self, email):
        msg = EmailMessage(email.subject, email.body, self.from_email, [email.email_to])
        msg.content_subtype = "html"
        msg.send()
        email.status = Email.STATUS_SENT
        email.save()
        return email

    def processing_emails(self):
        emails = email_service.get_all_not_sent_emails()
        for email in emails:
            try:
                self.send_email(email)
            except Exception as e:
                pass