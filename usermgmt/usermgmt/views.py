from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_user')
def charts(request):
    return render(request,"charts.html")

def home(request):
    return render(request,"home.html")
    
def register(request):
    msg={}
    if request.POST.get("uname") and request.POST.get("fname") and request.POST.get("lname") and request.POST.get("email") and request.POST.get("password") and request.POST.get("cpass"):
         print("in if")
         uname=request.POST.get("uname")
         fname=request.POST.get("fname")
         lname=request.POST.get("lname")
         email=request.POST.get("email")
         password=request.POST.get("password")
         cpass=request.POST.get("cpass")
         if password==cpass:
             print("same pass")
             if User.objects.filter(username=uname).exists():
                 msg={"msg":"User already exists"}
                 print(msg)
                 return render(request,"register.html",msg)
             else:
                 user=User.objects.create_user(username=uname,password=password,email=email,first_name=fname,last_name=lname)
                 user.set_password=password
                 user.save()
                 print("User got created")
                 return redirect("login_user")
         else:
             print("something went wrong")
             return redirect(register)
    else:
        return render(request,"register.html")

def login_user(request):
    msg={}
    print("hi in login...")
    if request.POST.get("uname") and request.POST.get("password"):
        print("in login if")
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=auth.authenticate(username=uname,password=password)
        if user:
            print("user ok")
            auth.login(request,user)
            return render(request,'home.html',{"msg":"Login Successful","flag":0})
        else:
            print("wrong input")
            msg={
                "msg":"Invalid User","flag":1
            }
            print(msg)
            return render(request,"login.html",msg)
    else:
        return render(request,"login.html",{"msg":""})

def logout_user(request):
    auth.logout(request)
    return redirect("home")

def setcookie(request):
    response=HttpResponse("Setting Cookies")
    response.set_cookie("city","Pune")
    return response
    
def getcookie(request):
    cookval=request.COOKIES.get("city")
    if cookval:
        return HttpResponse("<h2>Cookie value received ="+cookval)
    else:
        return HttpResponse("Coookies not found")
