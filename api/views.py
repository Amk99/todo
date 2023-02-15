# Create your views here.
from rest_framework import generics
from .models import Todo
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# View To diplay List of Tasks
class TaskList(generics.ListAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer


# Create New Task
class TaskCreateView(generics.CreateAPIView):
    model = Todo
    serializer_class = TodoSerializer
    def perform_create(self, serializer):
        serializer.save()


# Mark a task as Completed
class MarkAsCompleted(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(Todo ,pk=pk)
        todo.completed = True
        todo.save()
        return Response({'Message': 'Task marked as completed'}, status=status.HTTP_200_OK)


# Mark Task as incomplete
class MarkAsInComplete(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed = True
        todo.save()
        return Response({'Message': 'Task marked as Incomplete'}, status=status.HTTP_200_OK)


# Update Task
class update_todo(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(instance = todo,data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# Delete Task
class TaskDelete(APIView):
    def delete(self,request, pk):
        task = get_object_or_404(Todo,pk = pk)
        task.delete()
        return Response("Task deleted successfully.")

