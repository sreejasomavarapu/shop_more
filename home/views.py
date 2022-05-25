from email import message
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
# Create your views here.
def list(request):
    context={}
    return render(request,'home/list.html')

def detail(request):
    context={}
    return render(request,'home/detail.html',context)

def register(request):
    if request.method =="POST":
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request,f'Account has been created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context={'form':form}
    
    return render(request,'home/register.html',context)

def login(request):
    context={}
    return render(request,'home/login.html',)

def about(request):
    return render(request,'home/about.html')