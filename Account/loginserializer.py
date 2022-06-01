from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

class CustomLoginSerializer(LoginSerializer):
    phone_number = serializers.CharField()