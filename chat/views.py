import jwt

from django.http import HttpResponseForbidden
from django.shortcuts import render

from event_manager.decorators import jwt_required
from event_manager.settings import SECRET_KEY
from users.models import CustomUser


@jwt_required
def chat_index(request):
    current_user = request.user
    users = CustomUser.objects.exclude(pk=current_user.pk)
    return render(request, "chat/index.html", {"current_user": current_user, "users": users})

@jwt_required
def chat_room(request, room_name: str):
    token = request.headers.get('Authorization').removeprefix("Bearer ")
    current_user = request.user
    return render(
        request,
        "chat/room.html",
        {"current_user": current_user, "room_name": room_name, "token": token}
    )