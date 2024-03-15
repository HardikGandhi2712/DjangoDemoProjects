from django.http import HttpResponse
from django.shortcuts import render

def Delhi1(request):
    return render(request,"Delhi.html")

def gurudware1(request):
    return render(request,"gurudware.html")

def Monuments1(request):
    return render(request,"Monuments.html")

def temples1(request):
    return render(request,"temples.html")

def hello1(request):
    return render(request,"hello.html")
    
def filter(request):
    return render(request,"filters.html",{"ename":"vaNiTa is great","sal":[25000,29000,21000,10000]})

def fun1(request):
    return render(request,"fun1.html",{"empname":"vanita kale pune"})

def fun2(request):
    prod={
        "product":
        [
           ("Washing machine",40000),
           ("sofa",56000),
           ("TV",70000),
           ("Table",25000),
           ("Chair",4000)
        ]
    }
    return render(request,"fun2.html",prod)