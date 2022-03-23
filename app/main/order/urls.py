from django.urls import path, include
from .views import Hello

urlpatterns = [
    path('<str:username>/<int:productid>/', Hello.as_view()),
]
