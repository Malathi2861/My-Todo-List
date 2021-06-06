from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'content')

    def create(self, validated_data):
        data = validated_data.pop('content')
        output = Todo.objects.create(content=data)
        return output

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content')
        instance.save()
        return instance

    def delete(self, instance):
        instance.id = validated_data.get('id')
        instance.delete()
        return instance

