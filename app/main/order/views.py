from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView

from rest_framework.mixins import UpdateModelMixin

from ..models import Order, User, Product
from .serializer import OrderSerializer, OrderUpdateBankSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status

class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        user = User.objects.get(username=self.kwargs.get('username'))
        product = Product.objects.get(id=self.kwargs.get('productid'))
        serializer.save(user_id=user, product_id=product)

@api_view(['PUT'])
def update_order(request, pk, token):
    try: 
        order = Order.objects.get(pk=pk) 
    except Order.DoesNotExist: 
        return JsonResponse({'message': 'not found order'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        if int(token) == order.user_id.bank.token:
            data = JSONParser().parse(request) 
            serializer = OrderUpdateBankSerializer(order, data=data) 
            if serializer.is_valid(): 
                serializer.save() 
                return JsonResponse(serializer.data) 
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'invalid token'}, status=status.HTTP_404_NOT_FOUND) 