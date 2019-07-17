from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth import views as auth_views
import django.contrib.auth
from django.urls import path,include
from . import views


urlpatterns = [
    path('signup',views.signup,name = 'signup'),
    path('',include('django.contrib.auth.urls'))
]