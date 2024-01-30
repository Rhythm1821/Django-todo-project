from rest_framework import serializers
from todoapp import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Todo
        fields=('id','title','description')