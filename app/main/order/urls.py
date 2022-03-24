from django.urls import path, include
from .views import Hello, referal

urlpatterns = [
    path('ref/<int:productid>/', referal, name='referal'),
    path('<str:username>/<int:productid>/', Hello.as_view()),
]
