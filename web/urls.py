from . import views
from django.urls import path
urlpatterns = [
    path('login/' ,views.user_login),
    path('register/' ,views.register),
    path('dashboard/' , views.dashbord),
    path('test/' , views.test),
    path('' ,views.home ),    
]
