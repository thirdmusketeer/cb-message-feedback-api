from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'keywords', 'message', 'rating')


class MessageCreateSerializer(serializers.Serializer):
    class Meta:
        fields = ('keywords', 'message', 'rating')
