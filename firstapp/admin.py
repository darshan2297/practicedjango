from django.contrib import admin
from .models import student,book,register
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display = ['sno','sname','semail']

admin.site.register(student,studentadmin)

class bookadmin(admin.ModelAdmin):
    list_disp = ['bname','b_pic','price']

admin.site.register(book,bookadmin)

admin.site.register(register)

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

# admin.site.register(CustomUser,CustomUserAdmin)