from django.contrib import admin
from django.urls import path
from .views import TaskList,TaskCreateView,MarkAsCompleted, MarkAsInComplete

urlpatterns = [
    path('tasks',TaskList.as_view()),
    path('create',TaskCreateView.as_view()),
    path('complete/<int:pk>', MarkAsCompleted.as_view(), name='todo-complete'),
    path('incomplete/<int:pk>', MarkAsInComplete.as_view(), name='todo-complete'),

]
