from .consumers import *
from django.urls import path
wbs_urlpatterns=[
    path('ws/wsc/',ChatwbsConsumer.as_asgi()),
]