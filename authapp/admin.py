from django.contrib import admin
from .models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname','username','phone_no', 'email', 'password', 'rpsw']

    class Meta:
        model = Signup


admin.site.register(Signup,SignupAdmin)