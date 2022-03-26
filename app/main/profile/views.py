from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Order, User
from .serializer import SuccessOrderSerializer, ProfileSerializer

from ..auth.serializer import UserSerializer



class ProfileView(APIView):

    permission_classes = (IsAuthenticated,)   

    def get(self, request):
        user = User.objects.filter(username = request.user.username)
        success_order = Order.objects.filter(approval=True, user_id=request.user)
        #print(user, success_order)
        #print(user.id,user.username, user.bank, success_order)
        serializer_user = ProfileSerializer(user, many=True)
        serializer_order_success = SuccessOrderSerializer(success_order, many=True)
        #return Response({"Success order": serializer_order_success.data})
        return Response({"User": serializer_user.data, "Success order": serializer_order_success.data})
        