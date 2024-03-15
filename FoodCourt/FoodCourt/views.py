from .models import menu
from django.shortcuts import render

def insertmenu(request):
    if request.POST.get("menuname") and request.POST.get("category") and request.POST.get("rate"):
        rec=menu(menuname=request.POST.get("menuname"),category=request.POST.get("category"),photo=request.FILES["photo"],rate=int(request.POST.get("rate")))
        rec.save()
        return render(request,"AddMenu.html",{"msg":"Record Inserted"})
    return render(request,"AddMenu.html")

def menudisplay(request):
    st=menu.objects.all() # rec Collect all from table
    return render(request,'MenuDisplay.html',{'menu':st})