from django.urls import path
from.views import *

urlpatterns=[
    path('',home,name='register'),
    path('register',register,nmae='register'),
    path('user_login',user_login,name='user_login'),
    path('user_logout',user_logout,name='user_logout'),
    path('Event_Creation','Event_Creation',name='Event_Creation'),

]