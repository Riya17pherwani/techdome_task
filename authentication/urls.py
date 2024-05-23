from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LoginView, RegisterUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
