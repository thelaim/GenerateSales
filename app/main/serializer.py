'''from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
#from django.contrib.auth.models import User
from .models import Bank
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class CreateBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ('name')

    def create(self, validated_data):
        user = Bank.objects.create_bank(validated_data['name'])
        return bank

class BankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bank
        fields = '__all__'

        '''