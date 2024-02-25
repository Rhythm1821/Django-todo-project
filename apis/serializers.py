from rest_framework import serializers
from todoapp import models

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='todo-detail')
    class Meta:
        model=models.Todo
        fields=('id','url','title','description')

    def to_representation(self, instance):
        if self.context['view'].action=='retrieve':
            self.fields.pop('url')
        return super().to_representation(instance)