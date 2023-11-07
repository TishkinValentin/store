from django.contrib import admin
from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
]