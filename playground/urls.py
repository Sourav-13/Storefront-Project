from django.urls import path
from . import views

#UrlConf module
urlpatterns = [
    path("hello/", views.say_hello) #not calling the function, just passing the function's refference
]
