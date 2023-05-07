from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
# send_mail => for send one email for you
# send_mess_mail => for every one or send email for group


def send_email(subject, to, context, template_name):
    try:
        html_message = render_to_string(template_name, context)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    except:
        pass
