from django.db import models
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed
from Account.utils import sendwelcomeemail
# Create your views here.



@receiver(email_confirmed) # this is a signal that is sent when an email is confirmed
def email_confirmed_(request, email_address, **kwargs):
    new_email_address = EmailAddress.objects.get(email=email_address.email) # get the email address
    user = email_address.user      # get the user
    user.is_active = True          # set the user to active
    print(user, new_email_address)
    sendwelcomeemail(new_email_address, user) # send the welcome email
    user.save()                   # save the user