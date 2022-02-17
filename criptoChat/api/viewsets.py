from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from ..models import Group, Message
from .serializers import GroupSerializer, UserSerializer
from django.contrib.auth.models import User

from .mixin import GroupMixin, UserMixin

class GroupViewSet(GroupMixin,viewsets.ModelViewSet): 
	queryset=Group.objects.all()
	serializer_class=GroupSerializer
	permission_classes=(AllowAny, )


class UserViewSet(UserMixin,viewsets.ModelViewSet): 
	queryset=User.objects.all()
	serializer_class=UserSerializer
	permission_classes=(AllowAny, )
 
