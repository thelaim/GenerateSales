from django.urls import path, include
from .product.views import ProductView
from .profile.views import ProfileView
from .views import index

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('auth/', include('main.auth.urls')),
    path('order/', include('main.order.urls')),
    path('index/', index, name='index'),
]
