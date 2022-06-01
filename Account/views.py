from django.contrib.sites.shortcuts import get_current_site    
from allauth.account.adapter import DefaultAccountAdapter
# Create your views here.


class MyAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
            current_site = get_current_site(request)
            activate_url = self.get_email_confirmation_url(request, emailconfirmation)
            ctx = {
                "user": emailconfirmation.email_address.user,
                "activate_url": activate_url,
                "current_site": current_site,
                "key": emailconfirmation.key,
            }
            if signup:
                email_template = "email_confirmation"
            else:
                email_template = "email_confirmation"
            self.send_mail(email_template, emailconfirmation.email_address.email, ctx)