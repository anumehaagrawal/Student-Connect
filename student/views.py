from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from .analytics import recommend_college
from .models import *
from .forms import UserRegistrationForm, RecommendationForm, CounsellorForm

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

@login_required
def colleges(request):
	data = College.objects.all()
	nonelist = [None for i in range(5)]
	return render(request, 'student/colleges.html', {'colleges': data, 'ratings': nonelist})

@login_required
def recommendations(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            income = request.POST.get('income', '')
            ethnic_group = request.POST.get('ethnic_group', '')
            sat_score = request.POST.get('sat_score', '')
            gpa = request.POST.get('gpa', '')
            interest = request.POST.get('interest', '')
            recommended_colleges = recommend_college(int(income), interest, int(ethnic_group), int(sat_score))
            return render(request, 'student/result.html', {'data': recommended_colleges})
    else:
        form = RecommendationForm()
    return render(request, 'student/recommendation.html', {'form': form})

@login_required
def counsellors(request):
    if request.method == 'POST':
        form = CounsellorForm(request.POST)
        if form.is_valid():
            university = request.POST.get('university', '')
            counsellors_list = Counsellor.objects.filter(university=request.POST.get('university', ''))
            return render(request, 'student/counsellors_list.html', {'data': counsellors_list})
    else:
        form = CounsellorForm()
    return render(request, 'student/counsellor.html', {'form': form})
