from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'',views.MessageViewSet,"messages")

urlpatterns=router.urls