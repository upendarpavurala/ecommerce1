from django.test import TestCase
from productapp.models import Product



class ProductTestcase(TestCase):
    def setUp(self):
        Product.objects.create(pid=1, pcat=	'MOBILES', pname='iphone' ,pcost=25999.0000,
                               pdsc=1999.0000, pmfdt='2019-09-15', pexpdt='2029-09-15')

    def test_Product_info(self):
        s1=Product.objects.get(pid=1,pcost=25999.0000,)
        self.assertEqual(s1.get_productid(),1)
        self.assertEqual(s1. get_productcost(),25999.0000,)







