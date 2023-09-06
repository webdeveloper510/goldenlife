from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from adminapp.models import *


def get_value(request,user_obj):
    name=request.POST.get("name") 
    email=request.POST.get("email") 
    password=request.POST.get("password")
    confirm_password=request.POST.get("confirm")
    
    if password == confirm_password:
        user_obj.username=name
        user_obj.email=email
        user_obj.password=make_password(password)
        user_obj.user_type=1
        user_obj.save()
        return "save"
    return "error"


def login_value(request):
    username = request.POST.get('email') 
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)   
    if user:
        login(request, user)
        
        return "success"
    return "invalid"


def update_password(request):
    
    new_password=request.POST.get("new")
    confirm_password=request.POST.get("confirm")
    if new_password == confirm_password:
        User.objects.filter(id=request.user.id).update(password=make_password(new_password))

        return True
    return False   