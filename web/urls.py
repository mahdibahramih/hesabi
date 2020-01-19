from . import views
from django.urls import path
urlpatterns = [
    path('login/' ,views.user_login),
    path('register/' ,views.register),
    path('dashboard/' , views.dashbord),
    path('test/' , views.test),
    path('logout/',views.user_logout),
    path('profile/',views.profile),
    path('predict/',views.predict),
    path('report/',views.report),
    path('group/',views.group),
    path('send_expense/',views.send_expense),  
    path('send_income/',views.send_income),     
    path('addgroup/' , views.add_group),
    path('home/' ,views.home ), 
    
    
    path('' ,views.home ), 
]
