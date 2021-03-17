import json
from channels.generic.websocket import WebsocketConsumer
from django.http import response
from rest_framework.response import Response
from django.core import serializers
from django.contrib.auth import get_user_model

class ChatConsumer(WebsocketConsumer):
    def connect(self):
       
        self.accept()
        a= get_user_model().objects.all()
        self.send( serializers.serialize("json",queryset= a))

    def disconnect(self, close_code):
      
        pass

    def receive(self, text_data):
        print(text_data)
       
        # a=LoginSerializer(get_user_model().objects.all(),many=True)
        
        a= get_user_model().objects.all()
        self.send( serializers.serialize("json",queryset= a))