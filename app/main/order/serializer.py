from rest_framework import serializers
from ..models import Order, User, Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class OrderSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'income', 'email_client', 'phone', 'user_id', 'product_id')

class OrderUpdateBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('view', 'approval', 'id')