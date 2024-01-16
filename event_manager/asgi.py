"""
ASGI config for event_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing
from event_manager.middleware import WebSocketTokenMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_manager.settings')

event_manager_app = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": event_manager_app,
        "websocket": WebSocketTokenMiddleware(
            AuthMiddlewareStack(
                URLRouter(
                    chat.routing.websocket_urlpatterns
                )
            )
        )
    }
)

