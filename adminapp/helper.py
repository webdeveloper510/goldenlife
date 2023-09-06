from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect,HttpResponse

def send_forget_password_mail(email,token):
    subject="your forget password link"
    message=f'Hi,click on the link to reset your passord http://127.0.0.1:8000/Admin/change_password_link/{email}/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True


def verify_user_mail(email,token):
    subject="User verification email link"
    message=f'Hi,click on the link to verify the mail http://127.0.0.1:8000/verify_user_email/{email}/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)

    return HttpResponse("successfully")