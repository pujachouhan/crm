# from django.shortcuts import render
# from django.contrib.auth import login, authebticate
# from django.contribe.auth.forms import UserCreationForm,

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    return render(request,'home.html')


def register(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        user = User.objects.create_user(username=name,email=email,password=password)
        user.save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credential')
            return render(request,'home.html')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")