from authapp.models import Signin
from .models import Signup
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import http.client
import json
import random
#from django.views.generic.base import TemplateView


def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            x = otp_send(request)
            if x:
                return render(request, "otp_input.html")
            else:
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
def otpvalidation(request):
    newotp = request.POST["otp"]
    oldotp = request.session["otp"]
    if newotp== oldotp:
        form = SignUpForm(request.session['details'])
        new_user = User.objects.create_user(username=request.session['un'],password=request.session['pw'])
        new_user.save()
        form.save()
        login(request, new_user)
        return render(request,'signout.html')
    else:
        return render(request, 'otp_input.html')

def otp_send(request):
    ot = str(random.randint(100000, 999999))
    phone_no= request.POST["phone_no"]
    request.session["un"] = request.POST["username"]
    request.session["pw"] = request.POST["password"]
    request.session["details"] = request.POST
    request.session["otp"] = ot
    conn = http.client.HTTPConnection("api.msg91.com")
    payload = "{\"sender\": \"UPENDA\",\"route\": \"4\",\"country\": \"91\", \"sms\": [ { \"message\": \"" + ot + "\", \"to\": [ \"" + phone_no + "\"] } ] }"
    headers = {
        'authkey': "300132AMOiUNba6U5dadacdf",
        'content-type': "application/json"
    }
    conn.request("POST", "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encryt=&message=&flash&unicode=&schtime=&afterminutes=&response=&campaign=",payload, headers)
    data = conn.getresponse()
    res = json.loads(data.read().decode("utf-8"))
    print(res)
    if res["type"] == "success":
        return True
    else:
        return False

@login_required
def login(request):
    return render(request,"signout.html")
def my_logout(request):
    logout(request)
    return render(request,'index.html')

#def signin(request):
    #return render(request,"signin.html")




#class HomeView(TemplateView):

    template_name = 'index.html'


