from django.db.models import fields
from rest_framework import serializers
from . import models

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.MessageModel
        fields='__all__'


    def save(self, **kwargs):
        # print(self.validated_data)
        return super().save(**kwargs)