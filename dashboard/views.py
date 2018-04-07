from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .decorators import student_required, counsellor_required
from .forms import StudentSignUpForm, CounsellorSignUpForm, RecommendationForm, CounsellorForm
from .models import Counsellor, User, College
from django.utils import timezone
from django.http import JsonResponse
from .analytics import recommend_college,get_suggestions
from twilio.access_token import AccessToken,IpMessagingGrant


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
@student_required
def colleges(request):
    data = College.objects.order_by('title')
    nonelist = [None for i in range(5)]
    return render(request, 'student/college.html', {'colleges': data, 'ratings': nonelist})

@login_required
@student_required
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
            for col in range(len(recommended_colleges)):
            	recommended_colleges[col] = College.objects.get(title=recommended_colleges[col])
            return render(request, 'student/result.html', {'data': recommended_colleges})
    else:
        form = RecommendationForm()
    return render(request, 'student/recommendation.html', {'form': form})

@login_required
@student_required
def counsellors(request):
    if request.method == 'POST':
        form = CounsellorForm(request.POST)
        if form.is_valid():
            university = request.POST.get('university', '')
            counsellors_list = Counsellor.objects.filter(university=request.POST.get('university', ''))
            return render(request, 'counsellor/counsellors_list.html', {'data': counsellors_list})
    else:
        form = CounsellorForm()
    return render(request, 'counsellor/counsellor.html', {'form': form})

@login_required(login_url='/accounts')
def profile(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            return render(request, 'student/profile.html')
        else:
        	counsellor = Counsellor.objects.get(user=User.objects.get(username=request.user.username))
        	return render(request, 'counsellor/profile.html', { 'counsellor': counsellor })
    return redirect('/')

@login_required(login_url='/accounts')
def chat(request):
    return render(request,'student/chat.html')
@login_required
@student_required
def counsellors_profile(request, counsellor_username):
	if request.user.is_authenticated() and request.user.is_student:
		user_obj = User.objects.get(username=counsellor_username)
		counsellor_data = Counsellor.objects.get(user=user_obj)
		return render(request, 'counsellor/profile.html', { 'data': counsellor_data })
	return redirect('/')

@login_required
@student_required
def college_profile(request, number):
    if request.user.is_authenticated() and request.user.is_student:
        college_data = College.objects.get(id=int(number))
        college_name=college_data.title
        result=get_suggestions(college_name)
        res=[]
        for key in result:
            res.append(str(result[key]))
        print(res)
        return render(request, 'student/college_profile.html', { 'data': college_data,'extend_data':res })
    return redirect('/')

def token(request):
    device_id = request.GET.get('device', 'unknown')
    identity = request.GET.get('identity', 'guest').encode('utf-8')
    endpoint_id = "NeighborChat:{0}:{1}".format(device_id,identity)
    token = AccessToken(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_API_KEY,
                        settings.TWILIO_API_SECRET, identity)
    grant = IpMessagingGrant()
    grant.service_sid = settings.TWILIO_IPM_SERVICE_SID
    grant.endpoint_id = endpoint_id
    token.add_grant(grant)
    response = {'identity': identity, 'token': token.to_jwt()}
    return JsonResponse(response)