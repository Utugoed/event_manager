import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTING_MODULE", "events_manager.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

application = get_asgi_application()