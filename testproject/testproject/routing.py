from django.urls import re_path
from . import consumers

channel_routing = {re_path(r'', consumers.ChatConsumer.as_asgi())}