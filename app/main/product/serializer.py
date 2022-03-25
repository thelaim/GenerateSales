from dataclasses import fields
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

    def to_representation(self, instance):
        id = self.fields['id']
        id_value = id.to_representation(
            id.get_attribute(instance)
        )
        user =  self.context['request'].user
        data = super(ProductSerializer, self).to_representation(instance)
        return {
            'ref' : f"http://127.0.0.1:8000/api/order/{user.username}/{id_value}",
            'data' : data
        }
