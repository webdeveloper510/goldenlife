from django.urls import path
from healthapp import views


urlpatterns = [
    path("",views.home,name="home")
]
