import jwt

from django.http import HttpResponseForbidden
from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

from event_manager.settings import SECRET_KEY
from users.models import CustomUser



@authentication_classes([JWTAuthentication])
def chat_index(request):
    try:
        token = request.COOKIES.get('access_token')
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token['user_id']
        current_user = CustomUser.objects.get(pk=user_id)
    except Exception as ex:
        return HttpResponseForbidden("Access Forbidden: User not authenticated.")
    
    users = CustomUser.objects.exclude(pk=current_user.pk)
    return render(request, "chat/index.html", {"current_user": current_user, "users": users})

@authentication_classes([JWTAuthentication])
def chat_room(request, room_name: str):
    try:
        token = request.COOKIES.get('access_token')
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token['user_id']
        current_user = CustomUser.objects.get(pk=user_id)
    except Exception as ex:
        return HttpResponseForbidden("Access Forbidden: User not authenticated.")
    
    return render(request, "chat/room.html", {"current_user": current_user, "room_name": room_name, "token": token})