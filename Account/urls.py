from django.urls import path,include
from django.urls.conf import re_path
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path('confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
    ]