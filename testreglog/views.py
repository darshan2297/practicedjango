from django.shortcuts import render,redirect
from testreglog.forms import user_form,reg_form
from testreglog.models import user_reg
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        user_f = user_form(data=request.POST)
        reg_f = reg_form(data=request.POST)
        
        if user_f.is_valid() and reg_f.is_valid():
            user = user_f.save()
            user.set_password(user.password)
            user.save()
            
            reg = reg_f.save(commit=False)
            reg.user = user
            reg.save()
            
            return redirect('testreglog:user_login')
        else:
            print(user_form.errors,reg_form.errors)   
    else:
        user_f = user_form()
        reg_f = reg_form()
    return render(request,'register.html',{'user_f':user_f,'reg_f':reg_f})

def user_login(request):
    if request.method == 'POST':
        us = request.POST['uname']
        pwd = request.POST['password']
        
        user = authenticate(username=us,password=pwd)
        
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'login.html')
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('login failed')
        
    else:
        return render(request,'login.html') 
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'login.html')