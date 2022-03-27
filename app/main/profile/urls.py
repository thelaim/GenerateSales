from django.urls import path
from .views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('', ProfileView.as_view()),
    path('update/', ProfileUpdateView.as_view()),
]
