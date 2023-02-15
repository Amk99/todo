# Create your views here.
from rest_framework import generics
from .models import Todo
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class TaskList(generics.ListAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer

class TaskCreateView(generics.CreateAPIView):
    model = Todo
    serializer_class = TodoSerializer
    def perform_create(self, serializer):
        serializer.save()


class MarkAsCompleted(APIView):
    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.completed = True
        todo.save()
        return Response({'Message': 'Task marked as completed'}, status=status.HTTP_200_OK)


class MarkAsInComplete(APIView):
    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.completed = True
        todo.save()
        return Response({'Message': 'Task marked as Incomplete'}, status=status.HTTP_200_OK)