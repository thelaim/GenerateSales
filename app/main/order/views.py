from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import redirect



from ..models import Bank

#from .serializer import CreateBankSerializer, BankSerializer

class Hello(APIView):

    #permission_classes = (IsAuthenticated,)

    def get(self, request, username, productid):
        content = {'message': 'Hello, World!', 'orm': 'sdfsd', productid: username}
        return Response(content)

def referal(request, productid):
    name = request.user.username
    return redirect(f'http://127.0.0.1:8000/api/order/{name}/{productid}/')