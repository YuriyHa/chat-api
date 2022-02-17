from rest_framework import routers
from .viewsets import GroupViewSet, UserViewSet
from django.urls import path, include, re_path


router=routers.SimpleRouter()
app_name='api'
router.register(prefix=r'group', viewset=GroupViewSet)
router.register(prefix=r'user', viewset=UserViewSet)
# router.register(prefix=r'comment' , viewset=CommentViewSet)

urlpatterns =router.urls