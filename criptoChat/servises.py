from django.contrib.auth.models import User
from . import models 
import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
	## length of password from the user
	length = int(20)

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	return "".join(password)
# user setting method
def reg(data): 
    email = data['email']
    username = data['username']
    password = data['password']
    User.objects.get_or_create(email=email, username=username, password=password)
    user=User.objects.get(email=email)
    return user
def login(data):
    user=User.objects.get(username=data['username'],password=data['password']) 
    print(f"you logined to {user}...")
    return user
    
    
def creategroup(data): 
    user=login(data)
    permision_id=generate_random_password()
    group=models.Group.objects.create(admin=user,permision_id=permision_id)
    return group

def get_messages(data): 
    user=login(data)
    permision_id=data['api_key']
    group=models.Group.objects.get(permision_id=permision_id)
    if user in group.users.all(): pass
    else: group.users.add(user)
    messages=models.Message.objects.filter(group=group)
    return messages

def sendmessage(data): 
    user=login(data)
    
    permision_id=data['api_key']
    message_text=data['message_text']
    print(f'sending message "{message_text}"...')
    group=models.Group.objects.get(permision_id=permision_id)
    message=models.Message.objects.create(text=message_text, publisher=user, group=group)
    return message

def editmessage(data): 
    # user=login(data)
    
    message_text=data['message_text']
    id=data['message_id']
    print(f'editting message "{message_text}"...')
    message=models.Message.objects.get(id=id)
    
    message.text=message_text
    message.save()    
    
    return message


def removemessage(data): 
    user=login(data)
    id=data['message_id']
    message=models.Message.objects.get(id=id)
    if user==message.publisher: 
        message.delete()
    elif user==message.group.admin: 
        message.delete() 
    else: 
        return False 

def removegroup(data): 
    user=login(data)
    permision_id=data['api_key']
    group=models.Group.objects.get(permision_id=permision_id)
    if user==group.admin: 
        group.delete()  
    else: 
        return False 

def getgroup(data): 
    user=login(data)
    permision_id=data['api_key']
    group=models.Group.objects.get(permision_id=permision_id)
    return group 
    

def is_admin(obj, data): 
    user=login(data)
    return obj.admin == user

def new_group_message(obj, data): 
    user=login(data)
    group_messages=models.Message.objects.filter(group=obj)
    for i in group_messages: i.seen=(user in obj.seen.all() )
    return group_messages.filter(seen=False).count()
    
def new_message(obj, data): 
    user=login(data)
    
    if user in obj.seen.all(): 
        return True
    else: 
        obj.seen.add(user)
        return True
     
def list_member(data): 
    user=login(data)
    permision_id=data['api_key']
    group=models.Group.objects.get(permision_id=permision_id)
    return group.users.all()