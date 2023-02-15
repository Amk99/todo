# Create your views here.
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response


class TaskList(generics.ListAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer
