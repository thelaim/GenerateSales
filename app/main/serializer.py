from rest_framework import  serializers

from django.db import models
from .models import Bank


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
