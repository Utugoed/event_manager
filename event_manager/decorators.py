import jwt

from django.http import HttpResponseForbidden

from event_manager.settings import SECRET_KEY, SIMPLE_JWT
from users.models import CustomUser


def jwt_required(func):
    def wrap_view(request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return HttpResponseForbidden("Access Forbidden: User not authenticated.")
        try:
            cleared_token = token.removeprefix("Bearer ")
            decoded_token = jwt.decode(cleared_token, SECRET_KEY, algorithms=[SIMPLE_JWT["ALGORITHM"]])
            user_id = decoded_token['user_id']
            user = CustomUser.objects.get(pk=user_id)
        except (jwt.exceptions.DecodeError, KeyError):
            return HttpResponseForbidden("Access Forbidden: User not authenticated.")
        
        if not user:
            return HttpResponseForbidden("Access Forbidden: User not authenticated.")
        request.user = user
        return func(request, *args, **kwargs)
    return wrap_view