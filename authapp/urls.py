from authapp import views
from authapp.views import login
from django.conf.urls import url
from . import views
from django.urls import path
#from django.conf.urls import include, url
#from.import views
app_name='authapp'

urlpatterns=[
#url(r'^signin/$',views.signin),
path('signup/',views.signup),
path('login/',views.login),
path('my_logout/',views.my_logout),
url(r'^signup/otpvalidation$',views.otpvalidation),
#url(r'^$', views.HomeView.as_view(), name='home'),



]
