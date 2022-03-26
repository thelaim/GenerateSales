
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Product, User
from .serializer import ProductSerializer



class ProductView(APIView):

    permission_classes = (IsAuthenticated,)   

    def get(self, request):
        products = Product.product_objects.find_product(request.user.bank)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response({"product": serializer.data})
        


