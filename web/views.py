from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import expense , income , group , group_expense , group_income , group_member
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(req):
    return render(req , 'mainpage/index.html' , context=None)



@csrf_exempt
def login(request):
    if(request.method == 'GET'):
        return render(request ,'Login_v1/index.html')  
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "You're Logged in Successfully")
                return redirect('/accounts/dashboard/')
            else:
                messages.add_message(request, messages.ERROR, "Your account is disabled.")
                return redirect("/home/")
        else:
            messages.add_message(request, messages.ERROR, "Invalid login details supplied.")
            return redirect("/home")


@csrf_exempt     
def register(request):
    if(request.method == 'GET'):
        return render(request ,'register/index.html')  
    else:
        this_first_name = request.POST['first_name']
        this_last_name = request.POST['last_name']
        this_email = request.POST['your_email']
        this_username = request.POST['username']
        this_pass = request.POST['password']
        us =User.objects.create_user(username = this_username , email= this_email , password= this_pass , first_name = this_first_name , last_name = this_last_name )
        us.save()



@login_required
def add_group(req):
    new = group(name=req['group_name'] , discription=req['group_discription'] , admin=req.user )
    new.save()
