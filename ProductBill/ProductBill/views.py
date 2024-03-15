from django.shortcuts import render
from django.db import connection

def displayprod(request):
    cursor=connection.cursor()
    cursor.execute("select ono,orderdate,pname,price,qty from product,porder where product.pno=porder.pno order by ono")
    results=cursor.fetchall()
    return render(request,"pdisplay.html",{"porder":results})

def orderbill(request):
    cursor1=connection.cursor()
    cursor1.execute("select ono,orderdate,pname,price,qty from product,porder where product.pno=porder.pno order by ono")
    result1=cursor1.fetchall()
    cursor=connection.cursor()
    cursor.execute("select ono,sum(price*qty) from product,porder where product.pno=porder.pno group by ono order by ono")
    results=cursor.fetchall()
    return render(request,"orderbill.html",{"porder":results,"data":result1})