from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


def sendwelcomeemail(usermail, user):
    sending = send_mail(
				'Welcome to our site',
				strip_tags(render_to_string('welcomemail.html', {'name': user})), 
				settings.DEFAULT_FROM_EMAIL,
				[usermail], 
				html_message=render_to_string('welcomemail.html', {'name': user}))
    return sending