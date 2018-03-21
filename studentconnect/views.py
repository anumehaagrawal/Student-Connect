from django.shortcuts import render
from django.http import HttpResponse

def mainpage(request):
    return render(request, 'mainpage.html')

def counsellor_view(request):
	return HttpResponse("Counsellor auth non-existent currently. Coming soon.")