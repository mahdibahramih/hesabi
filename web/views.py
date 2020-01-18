from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create your views here.


def home(req):
    return render(req , 'mainpage/index.html' , context=None)

def login(req):
    if(req.method == 'GET'):
        return render(req ,'Login_v1/index.html')       
def register(req):
    if(req.method == 'GET'):
        return render(req ,'register/index.html')  