from django.contrib.auth.models import Permission
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
import json
from django.core import serializers as ok
from rest_framework import viewsets,response,renderers
from rest_framework.serializers import Serializer
from rest_framework.decorators import action, permission_classes
from . import serializers,models

# Create your views here.

class UserViewSet(viewsets.ViewSet):
   
  

    @action(detail=False,methods=['get'])
    def getActiveUsers(self,request):
        queryset=get_user_model().objects.all()
        serializer=serializers.LoginSerializer(queryset,many=True)
    
        return response.Response(serializer.data)



    @action(detail=False,methods=['get'])
    def isUserActive(self,request):
        queryset=get_user_model().objects.filter(phone_number="9705875179")
        if queryset.exists():
              if queryset[0].is_online:
                return response.Response( {'status':'1'})

              else :
                return response.Response({'status':'0'})
      




    @action(detail=False,methods=['post'])
    def register(s,f):
        Serializer=serializers.LoginSerializer(data=f.POST)
        if Serializer.is_valid(raise_exception=True):
            Serializer.save()
            return response.Response(Serializer.data)

        else :
                return response.Response(Serializer.errors)






    


       
   