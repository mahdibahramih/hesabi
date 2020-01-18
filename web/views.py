from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import expense , income , group , group_expense , group_income , group_member
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.


def home(req):
    return render(req , 'mainpage/index.html' , context=None)



@csrf_exempt
def user_login(request):
    if(request.method == 'GET'):
        return render(request ,'Login_v1/index.html')  
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.add_message(request, messages.ERROR, "Your account is disabled.")
                return redirect("/login/")
        else:
            messages.add_message(request, messages.ERROR, "Invalid login details supplied.")
            return redirect("/login/")


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
        return redirect("/login")



@login_required(login_url='/login/')
def add_group(req):
    new = group(name=req['group_name'] , discription=req['group_discription'] , admin=req.user )
    new.save()




@login_required(login_url='/login/')
def dashbord(request):
    return render(request , 'userpanel/mainpage.html')

@login_required(login_url='/login/')
@csrf_exempt
def test(req):
    return HttpResponse('hi')

def mainpage(req):
    if(req.method=='GET'):
        return render(req,'userpanel/mainpage.html') 

@csrf_exempt  
def send_expense(request):
    if(request.method=='POST'):
        User.objects.get(username=request.user.username)
        this_text=request.POST['subject']
        this_date=request.POST['date']
        this_time=datetime.datetime.now()
        this_amount=request.POST['cost']
        this_source=request.POST['source']      
        exp=expense.objects.create(user_name=request.user,text=this_text,time=this_time,date=this_date,amount=this_amount,sour=this_source)
        exp.save()

