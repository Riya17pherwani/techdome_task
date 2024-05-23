from django.urls import path
from .views import TodoCreateAPIView, TodoDestroyAPIView, TodoListAPIView, TodoRetrieveAPIView, TodoUpdateAPIView


urlpatterns = [
    path("getall", TodoListAPIView.as_view()),
    path("get/<pk>", TodoRetrieveAPIView.as_view()),
    path("put/<pk>", TodoUpdateAPIView.as_view()),
    path("create", TodoCreateAPIView.as_view()),
    path("delete/<pk>", TodoDestroyAPIView.as_view()),
]
