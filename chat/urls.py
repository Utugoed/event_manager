from django.urls import path

from chat.views import chat_index, chat_room


urlpatterns = [
    path("", chat_index),
    path("<str:room_name>/", chat_room)
]