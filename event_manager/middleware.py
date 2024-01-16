import jwt

from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from event_manager.settings import SECRET_KEY
from users.models import CustomUser


class WebSocketTokenMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = scope.get("query_string", b"").decode("utf-8")
        token = next((p.split("=")[1] for p in query_string.split("&") if "token=" in p), None)

        if token:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            scope['user'] = await self.get_user_from_token(decoded_token)
        else:
            scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)

    async def get_user_from_token(self, decoded_token):
        user_id = decoded_token.get('user_id')
        return await database_sync_to_async(CustomUser.objects.get)(id=user_id)

class CookiesToken2AuthHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        authorization_token = request.COOKIES.get('access_token')
        if authorization_token:
            request.META.update({"HTTP_AUTHORIZATION": f"Bearer {authorization_token}"})

#from django.http import HttpRequest
