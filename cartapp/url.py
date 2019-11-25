from django.conf.urls import url
from django.urls import path

from cartapp import views
app_name = 'cartapp'
urlpatterns = [
    url('addcart', views.addcart, name='search'),
    url('insertcart', views.insertcart, name='insertcart'),
    url(r'^cart', views.cart, name='cart'),
    url(r'^deletecart/', views.deletecart, name='deletecart'),
    url(r'^modifycart/', views.modifycart, name='modifycart'),
    url(r'^modifiedcart/', views.modifiedcart, name='modifiedcart'),

    ]

