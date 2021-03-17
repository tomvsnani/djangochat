from django import urls
from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'',views.UserViewSet,basename="usermodel")

urlpatterns=[
    path('',include(router.urls)),
    ]
