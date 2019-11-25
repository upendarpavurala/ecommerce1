from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from productapp.models import Stock, Product, Cart


@login_required
def addcart(request):
    x=request.GET["pid"]
    qt=Stock.objects.filter(prodid=x)
    qtt=0
    for p in qt:
        #global qtt
        qtt=p
    qt=[q for q in range(1,qtt.tot_qty+1)]
    return render(request,'addcart.html',{"pid":x,"qtt":qt})



def insertcart(request):
    x = request.GET["pid"]
    qt = request.GET["qt"]
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    pr = Product.objects.get(pid=x)
    a = int(str(x))
    b = int(str(qt))
    c = un
    d = float(pr.pcost)
    e = int(str(qt)) * float(pr.pcost)
    ct = Cart(username=c, pid=a, units=b, unitprice=d, tuprice=e)
    ct.save()
    stc = Stock.objects.get(prodid=x)
    stc.tot_qty = stc.tot_qty-b
    stc.save()
    return render(request, 'insertcart.html')
@login_required
def cart(request):
    return render(request, 'cart.html', display(request))


def display(request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    ct = Cart.objects.filter(username=un)


    tp = 0.0
    ctid = 0
    for p in ct:
        tp = tp + float(p.tuprice)
    ctid = p.id
    dic = {"k": ct, "tp": tp, 'ctid': ctid}
    return dic
def viewcart(request):
    return render(request, 'cart.html', display(request))

def deletecart(request):
    cs = Cart.objects.filter(id=int(request.GET["id"]))
    stc = Stock.objects.get(prodid = int(request.GET['pid']))
    stc.tot_qty = stc.tot_qty+int(request.GET['tot_qty'])
    stc.save()
    cs.delete()
    #return render(request, 'cart.html', display(request))
    return viewcart(request)


def modifycart(request):
    x = int(request.GET['pid'])
    qt = Stock.objects.filter(prodid=x)
    qtt = 0
    for p in qt:
        # global qtt
        qtt = p
    qt = [q for q in range(1, qtt.tot_qty + 1)]
    oldqt = request.GET["tot_qty"]
    cid = request.GET["id"]
    return render(request, 'modifyqty.html', {"cartid": cid, "pid": x, "qtt": qt, "oq": oldqt})

def modifiedcart(request):
    cid = int(request.GET["cid"])
    nqt = int(request.GET["nqt"])
    obj = Cart.objects.get(id=cid)
    stc = Stock.objects.get(prodid=int(request.GET['pid']))
    stc.tot_qty = stc.tot_qty-nqt+int(request.GET['oldqty'])
    stc.save()
    obj.units = nqt
    obj.save()
    up = obj.unitprice
    obj.tuprice = up * nqt
    obj.save()
    #cs = cart.objects.filter(pid=cid)
    return render(request, 'cart.html', display(request))
    #return viewcart(request)



