from django.shortcuts import render,redirect,HttpResponse
from adminapp.models import *
from django.contrib import messages
from adminapp.utils import *
from django.contrib import auth
from adminapp.helper import send_forget_password_mail,verify_user_mail
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
# Create your views here.


"""Dashboard Page"""

def AdminHome(request):
    return render(request,"admin/adminindex.html")




"""Fuction for user register"""
def AdminRegister(request):
    try:
        user_obj=User()    
        if request.method =="POST":
            regiser_value=get_value(request,user_obj)
            if regiser_value == "save":   
                messages.success(request, "Admin Register Successfully")
                return redirect("login")     
            messages.error(request, "Password didn't match")
            return redirect("register")   
        return render(request,"admin/register.html")
    except Exception as e:
        messages.error(request,"Email already exists")
        return redirect("register")   



"""Function for user login"""
def AdminLogin(request):
    if request.method == "POST":
        login_data=login_value(request)
        if login_data == "success":
            return redirect("dashboard")
        messages.error(request,"Invalid Credential",extra_tags='invalid')
    return render(request,"admin/adminlogin.html")



"""Function for user logout"""
def AdminLogout(request):
    auth.logout(request)
    return redirect("login")



"""Function for user profile"""
def AdminProfile(request):
    
    if request.method == "POST":
      
        update_data=update_password(request)
        if update_data==True:
            messages.success(request,"Password update")
            return redirect("profile")
        else:
            messages.error(request,"Password didn't match",extra_tags='invalid')
            return redirect("profile") 
    return render(request,"admin/profile.html")




"""forgot password to email link"""
def ForgotPassword(request):    
    if request.method=='POST':
        email=request.POST.get('email')
        
        if not User.objects.filter(email=email).first():
            return HttpResponse("1")   
        token=get_random_string(length=6, allowed_chars='0123456789')
        request.session['token'] = token
        send_forget_password_mail(email,token)    
        return HttpResponse("2")
    return render(request, "admin/forgot-password.html")


"""forgot password to email link"""
def ChangePasswordLink(request,email,token):  
    token2 = request.session['token']
    
    if request.method == "POST":
        password = request.POST.get('password')
        conpassword = request.POST.get('conpassword')
        if int(token) == int(token2):
            if password == conpassword:
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                request.session['token']=0
                msg="Password Changed Successfully."
                return render(request, "admin/adminlogin.html", {'msg':msg})
            msg="Your password and confirmation password do not match."   
            return render(request, "admin/changepassword.html", {'msg':msg})
        
        return HttpResponse("Invalid Link")
    return render(request, "admin/changepassword.html")



def ChangePassword(request):
    if request.method == "POST":
        password = request.POST.get('password')
        conpassword = request.POST.get('conpassword')
        if password == conpassword:
            user = User.objects.get(email=request.user.email)
            user.set_password(password)
            user.save()
            return HttpResponse("successfully")
        return HttpResponse("Your password and confirmation password do not match.")
    return render(request, "change_password.html")


def Appointments(request):
    return render(request,"admin/appointment-list.html")



def Specialities(request):
    return render(request,"admin/specialities.html")



def Doctor(request):
    return render(request,"admin/doctor-list.html")



def Patients(request):
    return render(request,"admin/patient-list.html")
    