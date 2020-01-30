from django.shortcuts import render,loader,redirect
from .forms import book1
from .models import book,register
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':"darshan how are you"})
    
def add(request):
    a = request.POST['num1']
    b = request.POST['num2']
    c = int(a)+ int(b)
    return render(request,'addtwo.html',{'c':c})

def display(request):
    info = book.objects.all()
    return render(request,'display.html',{'info':info})

def form(request): 
    if(request.method == 'POST'):
        fnm = request.POST['fname']
        lnm = request.POST['lname']
        unm = request.POST['uname']
        pwd = request.POST['pwd']
        ct = request.POST['city']
        st = request.POST['state']
        zipp = request.POST['zip']
        data = register(fname=fnm,lname=lnm,uname=unm,password=pwd,city=ct,state=st,zip= zipp)
        data.save()

        return render(request,'login.html')
    return render(request, "crispyform.html")

def success(request):
    display = register.objects.all()
    return render(request,'success.html',{'display':display})
    
# def simplesendemail(request):
#     # html_message = loader.render_to_string(
#     #         'success.html',
#     #         {
#     #             'message': 'We\'ll be contacting you shortly! If you have any questions, you can contact us at <a href="#">meow@something.com</a>',
#     #             'from_email': 'darshanvankawala2297@gmail.com',
#     #         }
#     #     )
#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'darshanvankawala2297@gmail.com',
#     ['kimeci3760@etopmail.com'],
#     fail_silently=False,
# )
    
#     return render(request,'success.html')
def login(request):
    #info = register.objects.all()
    if(request.method == 'POST'):
        unm = request.POST['uname'] 
        pwd = request.POST['password']
        
        count = register.objects.filter(uname=unm,password=pwd).count()
    
        if count > 0:
            request.session['is_logged'] = True
            request.session['user_id'] = register.objects.values('id').filter(uname=unm,password=pwd)[0]['id']
            return redirect('firstapp:home')
        else:
            return render(request,'login.html')
    return render(request,'login.html')   
        
def slug(request,slug):
    print(slug)
    return render(request,'success.html',{'slug':slug})

def logout(request):
    return redirect('accouts:signout')