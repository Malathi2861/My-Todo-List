from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'content')

    def get(self, validated_data):
        # profile_data = validated_data.pop('profile')
        # user = User.objects.create(**validated_data)
        # Profile.objects.create(user=user, **profile_data)
        data = validated_data.pop('content')
        output = Todo.objects.create(content=data)
        return output

    def update(self, instance, validated_data):

        instance.content = validated_data.get('email')
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance