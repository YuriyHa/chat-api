# likes/api/mixins.py
from matplotlib.style import context
from rest_framework.decorators import action
from rest_framework.response import Response
from .. import servises
from .serializers import MessageSerializer,GroupSerializer, UserSerializer
class GroupMixin:
    @action(detail=False,methods=['POST'])
    def get_group_messages(self, request): 
        data=request.data
        messages=servises.get_messages(data=data)
        serializer=MessageSerializer(messages, many=True,  context=request)
        return Response(serializer.data)
    
    @action(detail=False,methods=['POST'])
    def send_message(self, request): 
        data=request.data 
        messages=servises.sendmessage(data=data)
        serializer=MessageSerializer(messages,  context=request)
        return Response(serializer.data)
    
    
    @action(detail=False,methods=["POST"])
    def get_group(self, request): 
        data=request.data
        print('getting group...')
        group=servises.getgroup(data)
        serializer=GroupSerializer(group, context=request)
        return Response(serializer.data)
        
    @action(detail=False,methods=["POST"])
    def create_group(self, request): 
        data=request.data
        print('creating group...')
        group=servises.creategroup(data)
        serializer=GroupSerializer(group, context=request)
        return Response(serializer.data)
    
    @action(detail=False,methods=['POST'])
    def remove_group(self, request): 
        data=request.data
        servises.removegroup(data=data)
        return Response()

            
    @action(detail=False,methods=['POST'])
    def remove_message(self, request): 
        data=request.data
        servises.removemessage( data=data)
        return Response()
    
    @action(detail=False,methods=['POST'])
    def edit_message(self, request): 
        data=request.data
        print('editting message')
        message=servises.editmessage( data=data)
        serializer=MessageSerializer(message, context=request)
        return Response(serializer.data)
        
    @action(detail=False,methods=['POST'])
    def list_member(self, request): 
        # try:
        data=request.data
        members=servises.list_member(data=data)
        serializer=UserSerializer(members, many=True,  context=request)
        return Response(serializer.data)
        # except Exception as error:
        #     return Response(status=500)
        
class UserMixin: 
    @action(detail=False,methods=['POST'])
    def reg(self, request): 
        # try:
        data=request.data
        user=servises.reg(data=data)
        return Response()
        # except Exception as error:
        #     return Response(status=500)
