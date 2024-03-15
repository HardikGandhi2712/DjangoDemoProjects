from django.http import HttpResponse
from django.shortcuts import render, redirect
from Banking.models import acctrans
from Banking.models import account
from django.db import connection

def home_view(request):
    no_of_visits=request.session.get('no_of_visits',0)+1
    request.session['no_of_visits']=no_of_visits
    if no_of_visits>4: 
        del (request.session['no_of_visits'])
    return HttpResponse('<h2>Count of visits= '+str(no_of_visits))


def login1(request):
    if request.GET.get("uid") and request.GET.get("pass"):
        request.session["uid"]=request.GET.get("uid")
        request.session["pass"]=request.GET.get("pass")
        return redirect("/show")
    return render(request,"login1.html")


def getSessionData(request):
    uid=request.session.get("uid")
    password=request.session.get("pass")
    print(password)
    return render(request,"Show.html",{"uid":uid})


pin=0
bal=0
def login(request):
    if request.GET.get("accno") and request.GET.get("pin"):
        rec=account.objects.get(accno=int(request.GET.get("accno")),pin=request.GET.get("pin"))
        if rec:
            print("Found")
            request.session['ano']=request.GET.get("accno")
        return render(request,"Transaction.html")


def mini(request):
    acno=request.session.get("ano")
    cursor=connection.cursor()
    arec=account.objects.get(accno=acno)
    cursor.execute("select * from acctrans where accno=%s order by txdate desc limit 3",[acno])
    rec=cursor.fetchall()
    return render(request,"minist.html",{"rec":rec,"acno":acno,"abal":arec.balance})


def displogin(request):
    return render(request,"banklogin.html")


def addrec(request):
    msg={}
    print(request.session.get('ano'))
    if request.GET.get("txdate") and request.GET.get("txtype") and request.GET.get("amt"):
        acno=int(request.session.get("ano"))
        rec=acctrans(txdate=request.GET.get("txdate"),accno=acno,txtype=request.GET.get("txtype"),amount=request.GET.get("amt"))
        accrec=account.objects.get(accno=acno)
        accrec.accno=acno
          
        if request.GET.get("txtype")=='withdraw':
            b=accrec.balance
            print(b)
            print(b,b+1000,request.GET.get("amt"))
            if int(request.GET.get("amt"))>=(b-1000):
                print("in if..true")
                msg={"msg":"Insufficient Balance"}
            else:
                rec.save()
                accrec.balance=accrec.balance-int(request.GET.get("amt"))
                accrec.save()
                msg={"msg":"Transaction Successful..."}
        else:
                rec.save()
                accrec.balance=accrec.balance+int(request.GET.get("amt"))
                accrec.save()
                msg={"msg":"Transaction Successful..."}
    return render(request,"Transaction.html",msg)

