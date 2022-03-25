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

'''class UpdateOrderView(APIView):

    def put(self, request, productid, token, format=None):
        order = Order.objects.get(product_id=productid)
        if token == order.user_id.bank.token:
            serializer = OrderUpdateBankSerializer(order, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save(view=True)
                return JsonResponse(code=201, data=serializer.data)
            return JsonResponse(code=400, data="wrong parameters")


class UpdateOrderView(GenericAPIView,UpdateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateBankSerializer

    def put(self, request, *args, **kwargs):
        token = self.kwargs.get('token')
        pk = self.kwargs.get('pk')
        order = Order.objects.get(id=pk)
        if token == order.user_id.bank.token:
            return self.update(request, *args, **kwargs)'''

@api_view(['PUT'])
def update_order(request, pk, token):
    try: 
        order = Order.objects.get(pk=pk) 
    except Order.DoesNotExist: 
        return JsonResponse({'message': 'not found order'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        print(order.user_id.bank.token, token)
        if int(token) == order.user_id.bank.token:
            print('success')
            data = JSONParser().parse(request) 
            serializer = OrderUpdateBankSerializer(order, data=data) 
            if serializer.is_valid(): 
                serializer.save() 
                return JsonResponse(serializer.data) 
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'invalid token'}, status=status.HTTP_404_NOT_FOUND) 