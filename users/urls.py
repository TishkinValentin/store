from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registry, name='registry'),
    path('profile/', profile, name='profile'),
]
