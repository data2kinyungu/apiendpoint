from django.shortcuts import render

# Create your views here.
# class required to generate views

from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()