from rest_framework import viewsets

from todoapp import models
from .serializers import TodoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset=models.Todo.objects.all()    
    serializer_class=TodoSerializer