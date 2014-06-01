from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
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
                # msg = MIMEMultipart('alternative')
                # msg['Subject'] = email.subject
                # msg['From'] = from_email
                # msg['To'] = email.email_to
                # html = email.body
                # part = MIMEText(html.encode('utf-8'), 'html', 'utf-8')
                # msg.attach(part)
                # msg.content_subtype = "html"
                # server = smtplib.SMTP()
                # server.connect("smtp.gmail.com", "submission")
                # server.starttls()
                # server.ehlo()
                # server.login('no-reply@simzirok.com', 'SimZirok241')
                # server.sendmail(from_email, email.email_to, msg.as_string())
                # server.quit()
                email.status = Email.STATUS_SENT
                email.save()
                print 'all emails sent'
        except Exception, e:
            print e