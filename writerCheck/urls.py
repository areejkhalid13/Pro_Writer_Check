from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_fun,name="home"),
]
