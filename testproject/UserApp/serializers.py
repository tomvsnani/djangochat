from django.db.models.base import Model
from rest_framework import serializers
from django.contrib.auth import get_user_model

class LoginSerializer(serializers.ModelSerializer):
    okk=serializers.CharField(required=False)


    
    class Meta:
        model=get_user_model()
        exclude=['last_login','is_active','is_admin','is_superuser']
        extra_kwargs={'password':{'write_only':True}}
        


    # def validate(self, attrs):
    #     # print(attrs)
    #     return super().validate(attrs)

    # def validate_email(self,value):
    #     raise serializers.ValidationError("yesss")
    #     return value

    # def save(self, **kwargs):
    #     print(kwargs)
    #     user=  get_user_model().objects.create_user()
    #     return user

    def create(self, validated_data):
        user=  get_user_model().objects.create_user(**validated_data)
        return user


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

   

        