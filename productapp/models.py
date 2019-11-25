from django.db import models
from django.utils import timezone

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pcat = models.CharField(max_length=30)
    pname = models.CharField(max_length=30)
    pcost = models.DecimalField(max_digits=10,decimal_places=4)
    pdsc = models.DecimalField(max_digits=10, decimal_places=4)
    pmfdt = models.DateField()
    pexpdt = models.DateField()


    def __str__(self):
        return str(self.pid)

    def get_productcost(self):
        return self.pcost

    def get_productid(self):
        return self.pid

class Stock(models.Model):
    prodid = models.OneToOneField(
        Product,
        on_delete= models.CASCADE,
        primary_key=True,
    )
    tot_qty = models.IntegerField()
    last_update = models.DateField()
    next_update = models.DateField()

class Cart(models.Model):
        username = models.CharField(max_length=20)
        pid = models.IntegerField()
        units = models.IntegerField()
        unitprice = models.DecimalField(max_digits=10, decimal_places=4)
        tuprice = models.DecimalField(max_digits=10, decimal_places=4)





