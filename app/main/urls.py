from django.urls import path, include
from .product.views import ProductView
from .views import index

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('profile/', include('main.profile.urls')),
    path('auth/', include('main.auth.urls')),
    path('order/', include('main.order.urls')),
    #path('index/', index, name='index'), # этот endpoint для просмотра токена банков
]
