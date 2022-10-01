from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from message.views import AISuggestionAPI, RateAPI, MessagesListAPI

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'', schema_view),
    path("ai/message/", AISuggestionAPI.as_view()),
    path("ai/rate/", RateAPI.as_view()),
    path("ai/messages/", MessagesListAPI.as_view()),
]
