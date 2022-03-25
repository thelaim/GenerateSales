from django.urls import path
from .views import CreateOrderView, update_order #UpdateOrderView, update_order

urlpatterns = [
    path('ref/<str:username>/<int:productid>/', CreateOrderView.as_view()),
    #path('<int:pk>/<str:token>/', UpdateOrderView.as_view()),
    path('<int:pk>/<str:token>/', update_order),
]

#productid
