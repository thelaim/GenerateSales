from django.urls import path, include
from .views import Hello, index

urlpatterns = [
    path('', Hello.as_view()),
    path('index', index, name='index'),
]
