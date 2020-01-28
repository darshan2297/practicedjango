from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from accouts.models import user
from accouts.forms import authform

def signup(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def signin(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('firstapp:home')
    else:
        form =  AuthenticationForm()
    return render(request,'signin.html',{'form':form})
# Create your views here.

def signout(request):
    logout(request)
    return redirect('firstapp:home')

@login_required(login_url="accouts:signin")
def create_ac(request):
    return render(request,'create_ac.html')

def user_detail(request):
    users = user.objects.all()
    data = {'users':users}
    return render(request,'user_detail.html',context=data)

def form_auth(request):
    forms = authform(request.POST)
    if(request.method == 'POST'):
        if(forms.is_valid()):
           print("Username:"+forms.cleaned_data['Username'])
           print("Password:"+forms.cleaned_data['Password'])
           print("Firstname:"+forms.cleaned_data['First_name'])
           print("Lastname:"+forms.cleaned_data['Last_name'])
           print("Emailaddress:"+forms.cleaned_data['Email_address'])
        else:
            print('Error')
    return render(request,'authform.html',{'forms':forms})