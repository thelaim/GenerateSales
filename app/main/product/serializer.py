from rest_framework import  serializers

from django.db import models
from ..models import Product, CategoryProduct, Bank

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    bank = BankSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'