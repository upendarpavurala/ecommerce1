from django.test import TestCase
from authapp.models import Signin,Signup
from django.test import TestCase,client
from django.urls import reverse
import json


class SigninTestcase(TestCase):
    def setUp(self):
        Signin.objects.create(username='hii',password='haihello')
    def test_signin_info(self):
        s1=Signin.objects.get(username='hii',password='haihello')
        self.assertEqual(s1.get_user(),'hii')
        self.assertEqual(s1.get_pswd(),'haihello')


class SignupTestcase(TestCase):
    def setUp(self):
        Signup.objects.create(firstname ='hai', lastname ='hello', username='hai',
                              phone_no=9848441725 ,email='upendar342@gmail.com', password='haihello' ,rpsw='haihello')
    def test_signup_info(self):
        s2=Signup.objects.get(phone_no =9848441725)
        self.assertEqual(s2.get_mobile(),9848441725)





        
class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_signuppage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)




