
from tkinter import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
import qrcode

# from django.views.generic import ListView
# from .models import UserForm


@login_required(login_url='/signin')
def index(request):
    img = ''

    new_form = forms.UserDisplayForm()
    if request.method == 'POST':
        # new_form = forms.UserDisplayForm(request.POST)
        data = request.POST['email']
        # print(data)
        # data = forms.UserDisplayForm(request.POST['email'])
        img = qrcode.make(data)
        # img = qrcode.make(new_form)
        img.save('generator/static/img/qrcode.png')
    else:
        data = ''
    user_dict = {'forms': new_form, 'message': data, 'img': img}

    # return HttpResponse(render(request, 'generator/index.html', user_dict))
    return render(request, 'generator/index.html', user_dict)


# import qrcode

# Create your views here.
# data = None

# def index(request):
#     global data
#     if request.method == 'POST':
#         data = request.POST['data']

#         img = qrcode.make(data)
#         img.save('file.png')
#     return render(request, 'generator/index.html')


# class HomePageView(ListView):
#     model = UserForm
#     template_name= ('generator/index.html')

def signup(request):  # for Register
    signupform = forms.RegistrationForm()
    if request.method == 'POST':
        signupform = forms.RegistrationForm(request.POST)
        if signupform.is_valid():
            password = signupform.cleaned_data['password']
            confirm_password = signupform.cleaned_data['confirm_password']
            if password != confirm_password:
                print('Password does not match')
            else:
                signupform.save()
                new_user = User.objects.get(
                    username=signupform.cleaned_data['username'])
                new_user.set_password(password)
                # new_user.active = True
                new_user.save()
    user_dict = {'forms': signupform}
    return render(request, 'generator/register.html', user_dict)


def signin(request):  # for Login
    signinForm = forms.LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    user_dict = {'forms': signinForm}
    return render(request, 'generator/login.html', user_dict)


@login_required(login_url='/signin')
def log_out(request):
    logout(request)
    return redirect('signin')
