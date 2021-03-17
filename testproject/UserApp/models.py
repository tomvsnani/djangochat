from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from rest_framework.fields import ReadOnlyField

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self,phone_number,password=None,**kwargs):
        if not phone_number or len(phone_number)!=10:
            raise ValueError("phone_number umber must not be null")
        user=self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone_number,password=None):
         if not phone_number or len(phone_number)!=10:
            raise ValueError("phone_number umber must not be null")
         
         user=self.create_user(phone_number,password)
         user.is_admin=True
         user.is_superuser=True
         user.is_active=True
         user.save(using=self._db)

         return user

    

class CustomUserModel(AbstractBaseUser):
    phone_number=models.CharField(max_length=60,unique=True)
    username=models.CharField(max_length=60,blank=True)
    email=models.CharField(max_length=60,blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    last_seen=models.DateTimeField(auto_now=True)
    is_online=models.BooleanField(default=False,blank=False)

    objects=UserManager()

    USERNAME_FIELD="phone_number"
    REQUIRED_FIELDS=[]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class UserModelTest(models.Model):
    phone_number=models.CharField(max_length=60,unique=True)
    username=models.CharField(max_length=60)
    email=models.CharField(max_length=60)




    



   
    
    

