from dataclasses import field
from rest_framework import serializers
from ..models import Order, User, Product

from ..product.serializer import BankSerializer

class ProductOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name']

class SuccessOrderSerializer(serializers.ModelSerializer):
    product_id = ProductOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    bank = BankSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'bank', 'first_name', 'last_name')