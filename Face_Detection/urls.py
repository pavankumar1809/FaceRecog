from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name = "home"),
    path('register/',register,name = 'register'),
    path('register/enable/<face_id>/',enableFace,name = 'enable'),
    path('login/',login,name = 'login'),
    path('greeting/<face_id>/',Greeting,name='greeting')
]
