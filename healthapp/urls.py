from django.urls import path
from healthapp import views


urlpatterns = [
    path("",views.Home,name="home"),
    path("blog",views.Blog,name="blog"),
    path("register",views.Register,name="userregister"),
    path("login",views.Login,name="userlogin"),
    path("doctor",views.DoctorDashboard,name="doctors"),
    path("appoint",views.Appointment,name="appoint"),
    path("schedule",views.Schedule,name="schedule"),
    path("patient",views.Patient,name="doctorpatient")
]
