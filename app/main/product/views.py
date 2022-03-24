from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Product, User
from .serializer import ProductSerializer

class ProductView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        products = Product.objects.filter(bank=request.user.bank)
        serializer = ProductSerializer(products, many=True)
        return Response({"product": serializer.data, "Реферальная ссылка на оформление заявки": f"http://127.0.0.1:8000/api/order/{request.user.username}/3/"})
