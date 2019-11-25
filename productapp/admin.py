from django.contrib import admin
from .models import Product,Stock
class Productadmin(admin.ModelAdmin):
    list_display = ['pid','pname','pcat','pcost','pdsc','pmfdt','pexpdt']
    list_filter = ['pcat','pmfdt','pexpdt']
    class Meta:
        model = Product
admin.site.register(Product,Productadmin)

class Stockadmin(admin.ModelAdmin):
    list_display = ['prodid','tot_qty','last_update','next_update']
    list_filter = ['prodid']
    class Meta:
        model = Stock
admin.site.register(Stock,Stockadmin)