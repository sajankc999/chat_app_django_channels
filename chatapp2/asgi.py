"""
ASGI config for chatapp2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from chatapp.routers import *
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp2.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application() ,
    'websocket':URLRouter(wbs_urlpatterns)
})
