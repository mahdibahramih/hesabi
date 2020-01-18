from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create your views here.


def home(req):
    return render(req , 'mainpage/index.html' , context=None)