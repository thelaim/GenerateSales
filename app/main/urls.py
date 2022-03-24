from django.urls import path, include
from .product.views import ProductView

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('auth/', include('main.auth.urls')),
    path('order/', include('main.order.urls')),
]
