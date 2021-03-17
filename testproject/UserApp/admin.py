from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

class UserAdmin(UserAdmin):
    list_display=['id','username','phone_number','is_admin','last_seen','is_online','password']
    list_filter=['phone_number']
    fieldsets=(
        (None, {'fields':('phone_number','is_online','username','email')}),
      
        )
    add_fieldsets=((None,({"fields":('phone_number')})))

    filter_horizontal=()

admin.site.register(models.CustomUserModel,UserAdmin) 

 



# Register your models here.
