from rest_framework import viewsets,generics

from todoapp.models import Todo
from .serializers import TodoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()    
    serializer_class=TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer