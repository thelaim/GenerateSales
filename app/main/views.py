from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.http import HttpResponse

from .models import Bank


def index(request):

    query = Bank.objects.first()
    content = {'Bank token': query.token}
    return HttpResponse(query.token)
