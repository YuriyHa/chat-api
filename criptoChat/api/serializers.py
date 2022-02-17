from grpc import services
from rest_framework import serializers

from ..models import Group, Message
from .. import servises as serv

class GroupSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()
    new_message=serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = (
            'id',
            'permision_id',
            'is_admin',
            'new_message', 
            'users', 
        )
        
    def get_is_admin(self, obj): 
        try: return serv.is_admin(obj, self.context.data)
        except: return False 

     
    def get_new_message(self, obj): 
        try: return serv.new_group_message(obj, self.context.data)
        except: return False 

class MessageSerializer(serializers.ModelSerializer):
    new_message=serializers.SerializerMethodField()
    class Meta:
        model =Message
        fields = (
            'id',
            'text',
            'time',
            'publisher',
            'new_message', 
            'seen', 
        )
    def get_new_message(self, obj): 
        try: return serv.new_message(obj, self.context.data)
        except: return False 

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
        )


from django.contrib.auth import get_user_model
