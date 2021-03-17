from django.db import models
from django.contrib.auth import get_user_model

class MessageModel(models.Model):
    messageText=models.TextField(blank=True)
    timeSent=models.DateTimeField(auto_now_add=True)
    timeDelivered=models.DateTimeField(blank=True,null=True)
    timeRead=models.DateTimeField(blank=True,null=True)
    messagestatus=models.CharField(max_length=4,default="1")
    imageField=models.ImageField(upload_to='images',null=True)
    sender=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="send")
    receiver=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="receiver",default='empty')

    def __str__(self) -> str:
        return f'{self.sender.username} to {self.receiver.username}'



# class CommonIdModel(models.Model):
#     user1=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
#     user2=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    

# Create your models here.
