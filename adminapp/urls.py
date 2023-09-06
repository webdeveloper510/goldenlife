from django.urls import path
from adminapp import views


urlpatterns = [
    path("",views.AdminRegister,name="register"),
    path("login/",views.AdminLogin,name="login"),
    path("dashboard/",views.AdminHome,name="dashboard"),
    path("logout/",views.AdminLogout,name="logout"),
    path("profile/",views.AdminProfile,name="profile"),
    path("forget/",views.ForgotPassword,name="forget"),
    path("change_password_link/<str:email>/<int:token>",views.ChangePasswordLink,name="change_password_link"),
    path("change_password",views.ChangePassword,name="change_password"),
    path("appointment",views.Appointments,name="appointment"),
    path("specialities",views.Specialities,name="specialities"),
    path("doctor",views.Doctor,name="doctor"),
    path("patients",views.Patients,name="patients"),
]
