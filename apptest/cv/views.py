from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UploadedFile
from .forms import UploadFileForm

def homepage(request):

    return render(request, 'cv/index.html')



def register(request):

    if request.method == "GET":
        
        form = CreateUserForm()

    context = {'register': form}

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")

            return redirect('my_login')

    context = {'registerform':form}


    return render(request, 'cv/register.html', context=context)

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')


    context = {'loginform':form}


    
    return render(request, 'cv/my_login.html', context=context)
    

def user_logout(request):

    auth.logout(request)

    return redirect("")


def dashboard(request):


    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
        images = UploadedFile.objects.all()
    return render(request, 'cv/dashboard.html')