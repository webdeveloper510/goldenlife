from django.shortcuts import render


# Create your views here.


def Home(request):
    return render(request,"index.html")


def Blog(request):
    return render(request,"blog-list.html")


def Register(request):
    return render(request,"register.html")


def Login(request):
    return render(request,"login.html")


def DoctorDashboard(request):
    return render(request,"doctor-dashboard.html")


def Appointment(request):
    return render(request,"appointments.html")


def Schedule(request):
    return render(request,"schedule-timings.html")


def Patient(request):
    return render(request,"my-patients.html")
    
    