from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from authentication.permissions import IsAdmin, IsUserOrAdmin
from .serializers import TodoSerializer
from .models import Todo


class TodoListAPIView(ListAPIView):
    permission_classes = [IsUserOrAdmin]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAdmin]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreateAPIView(CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
