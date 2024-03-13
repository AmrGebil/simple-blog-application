# from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Account



class AccountRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


