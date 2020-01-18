from . import views
from django.urls import path
urlpatterns = [
    path('login/' ,views.user_login),
    path('register/' ,views.register),
    path('dashboard/' , views.dashbord),
    path('test/' , views.test),
    path('' ,views.home ), 
    path('mainpage/',views.mainpage),
    path('send_expense/',views.send_expense),      
]
