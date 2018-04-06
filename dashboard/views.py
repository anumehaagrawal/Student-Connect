from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .decorators import student_required, counsellor_required
from .forms import StudentSignUpForm, CounsellorSignUpForm, RecommendationForm, CounsellorForm
from .models import Counsellor, User, College
from django.utils import timezone
from .analytics import recommend_college

class CounsellorSignUpView(CreateView):
    model = Counsellor
    form_class = CounsellorSignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request, 'home.html')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        user.last_login = timezone.now()
        login(self.request, user)
        return render(self.request, 'home.html')

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def colleges(request):
    data = College.objects.order_by('title')
    nonelist = [None for i in range(5)]
    return render(request, 'student/college.html', {'colleges': data, 'ratings': nonelist})

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
            print(counsellors_list[0].university)
            return render(request, 'counsellor/counsellors_list.html', {'data': counsellors_list})
    else:
        form = CounsellorForm()
    return render(request, 'counsellor/counsellor.html', {'form': form})

@login_required(login_url='/accounts')
def profile(request):
    if request.user.is_authenticated() and request.user.is_student:
        return render(request, 'student/profile.html')
    return redirect('/')
