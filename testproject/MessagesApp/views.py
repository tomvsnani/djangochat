from django.contrib.auth import get_user_model
from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import MessageModel
import socket
import json

class MessageViewSet(viewsets.ModelViewSet):

    serializer_class=MessageSerializer
    queryset=MessageModel.objects.all()

    @action(detail=False,methods=['post'])
    def insertmessage(self,request):
        # if not CommonIdModel.objects.filter(user1=request.POST.get('sender'),user2=request.POST.get('receiver')).exists():
            
        
        a=request.data


        dictt=json.loads(a['data'])
        dictt['imageField']=a['imageField']
        
        print(dictt)
        
        serializerLocal=MessageSerializer(data=dictt)
        
        
        if serializerLocal.is_valid(raise_exception=True):
            serializerLocal.save()
            
            return Response(serializerLocal.data)
        else :
            return Response({'status':'0'})



    @action(detail=False,methods=['post'])
    def getmessage(self,request):

        queryset=MessageModel.objects.filter(
            
            Q(sender=request.POST.get('sender')) & Q(receiver=request.POST.get('receiver')) |

            (Q(sender=request.POST.get('receiver')) & Q(receiver=request.POST.get('sender')))

       ).order_by('id')

        # for i in range(100000):
        #     if i%2==0:
        #         MessageModel.objects.create(sender=get_user_model().objects.get(id='21'),receiver=get_user_model().objects.get(id='1'),messageText="hello")
        #     else :
        #         MessageModel.objects.create(sender=get_user_model().objects.get(id='1'),receiver=get_user_model().objects.get(id='21'),messageText="hello")



        # print(queryset[0])

        serializerLocal=MessageSerializer(queryset,many=True)

        return Response(serializerLocal.data)



    @action(detail=False,methods=['post'])
    def set_message_as_read(self,request):
        query=MessageModel.objects.filter(sender=request.POST.get('sender'),receiver=request.POST.get('receiver')).exclude(messagestatus="3")

        for i in query:
            i.messagestatus="3"
            i.save()

        return Response("1")


    @action(detail=False,methods=['get'])
    def getUserId(self,request):
        return Response("17")

    # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # s.bind(('127.0.0.1',8000))
    # s.listen()
    # while True:
    #     s.accept()
    #     print("accepted")


    

        

# Create your views here.
