from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.http import HttpResponse

from .models import Bank

#from .serializer import CreateBankSerializer, BankSerializer

def index(request):
    #permission_classes = (IsAuthenticated,)

    query = Bank.objects.first()
    content = {'message': 'Hello, World!', 'orm': query.token}
    return HttpResponse(query.token)

    #query = Bank.objects.first()
    #return HttpResponse(f'{query.name}: {query.token}')


class Hello(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!', 'orm': 'sdfsd'}
        return Response(content)

