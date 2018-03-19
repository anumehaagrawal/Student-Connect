from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'student/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/student')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})

@login_required(login_url='/student/login/')
def profile(request):
	return render(request, 'student/profile.html')

@login_required
def logout_view(request):
	logout(request)
	return render(request, 'registration/logout.html')
