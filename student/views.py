from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,StudentProfile
import requests
from pprint import pprint
import numpy as np
from nltk.corpus import wordnet
from itertools import product

subscription_key="a0cdcb30c0894f918d92c0de8f34d85e"
assert subscription_key 
text_analytics_base_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0" 
sentiment_api_url = text_analytics_base_url + "/sentiment"

documents={}

documents['documents']=[]
def add(college_name,reviews,lang):

    arr=documents.get('documents')
    arr.append({'id': college_name, 'language':lang,'text':reviews})
    
add('nitk','This is an amazing college but infras is bad','en')

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)

sentiments = response.json()
pprint(sentiments)

def home(request):
    return render(request, 'student/home.html')

def display(request):
    return render(request,'student/display.html')

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
    if request.method == 'POST':
        form = StudentProfile(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/student/profile_display')
            print("valid")
    else:
        form = StudentProfile()
        return render(request, 'student/profile.html', {'form_set': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
