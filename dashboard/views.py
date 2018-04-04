from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .decorators import student_required, counsellor_required
from .forms import StudentSignUpForm, CounsellorSignUpForm
from .models import Counsellor, User, College
from django.utils import timezone


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
