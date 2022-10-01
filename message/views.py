from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from ai_client import get_suggestions
from .models import Message
from .serializers import MessageSerializer


# {
# 	"keywords": "スキンケア, クーポン"
# }
class AISuggestionAPI(APIView):
    def post(self, request, format=None):
        keywords = request.data.get("keywords")
        if keywords:
            suggestions = get_suggestions(keywords)
            return Response(suggestions, status=status.HTTP_200_OK)
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "keywords (comma separated) can't be empty"
        }, status=status.HTTP_400_BAD_REQUEST)


# {
# "keywords": "スキンケア, クーポン",
# 	"message": "【クーポンのご提案】 3問の中で、案内を見て",
#   "rate": true
# }
class RateAPI(APIView):
    def post(self, request, format=None):
        message = request.data.get("message")
        rate = request.data.get("rate")
        keywords = request.data.get("keywords")
        if message and type(rate) == bool and keywords:
            new_message = Message.objects.create(
                keywords=keywords,
                message=message,
                rating=rate
            )
            new_message_serialize_data = MessageSerializer(new_message).data
            print(message, rate)
            return Response(new_message_serialize_data, status=status.HTTP_201_CREATED)
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "params message,rate, keywords can't be empty"
        }, status=status.HTTP_400_BAD_REQUEST)


class MessagesListAPI(ListAPIView):
        queryset = Message.objects.all()
        serializer_class = MessageSerializer
