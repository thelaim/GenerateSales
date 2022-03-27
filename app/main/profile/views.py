from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Order, User
from .serializer import SuccessOrderSerializer, ProfileSerializer

from ..auth.serializer import UserSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status



class ProfileView(APIView):

    permission_classes = (IsAuthenticated,)   

    def get(self, request):
        user = User.objects.filter(username = request.user.username)
        success_order = Order.objects.filter(approval=True, user_id=request.user)
        serializer_user = ProfileSerializer(user, many=True)
        serializer_order_success = SuccessOrderSerializer(success_order, many=True)
        return Response({"User": serializer_user.data, "Success order": serializer_order_success.data})

class ProfileUpdateView(APIView):

    permission_classes = (IsAuthenticated,)   

    def put(self, request):
        try: 
            user = User.objects.get(username=request.user.username) 
        except User.DoesNotExist: 
            return JsonResponse({'message': 'Not found user'}, status=status.HTTP_404_NOT_FOUND) 
 
        if request.method == 'PUT': 
            data = JSONParser().parse(request) 
            serializer = ProfileSerializer(user, data=data) 
            if serializer.is_valid(): 
                serializer.save() 
                return JsonResponse(serializer.data) 
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'Not "PUT"'}, status=status.HTTP_404_NOT_FOUND)
        