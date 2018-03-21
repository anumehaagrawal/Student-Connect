from django import forms
from .models import College

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = 'Username',
		max_length = 32
	)
	email = forms.CharField(
		required = True,
		label = 'Email',
		max_length = 32,
	)
	password = forms.CharField(
		required = True,
		label = 'Password',
		max_length = 32,
		widget = forms.PasswordInput()
	)

class RecommendationForm(forms.Form):
	ETHNIC_SELECT = [
		(0, 'American Indian/Alaskan Native'),
		(1, 'Asian'),
		(2, 'Black/African-American'),
		(3, 'Hispanic/Latino'),
		(4, 'Multi-race (not Hispanic/Latino)'),
		(5, 'Native Hawaiian/ Pacific Islander'),
		(6, 'White'),
		(7, 'Unknown'),
	]
	income = forms.IntegerField(
		required = True,
		label = 'Income (in lakhs per annum)',
	)
	interest = forms.CharField(
		required = True,
		label = 'Interest (eg. teaching;computer science;football)',
		max_length = 255,
	)
	sat_score = forms.IntegerField(
		required=True,
		label='SAT Score',
	)
	gpa = forms.DecimalField(
		required=True,
		label='GPA (scaled out of 4)',
	)
	ethnic_group = forms.ChoiceField(
		label="Ethnicity",
		required=True,
		choices=ETHNIC_SELECT,
	)

class CounsellorForm(forms.Form):
	COLLEGE_SELECT = College.objects.values_list('title', flat=True)
	COLLEGE_SELECT = [(i, i) for i in COLLEGE_SELECT]

	university = forms.ChoiceField(
		label="University",
		required=True,
		choices=COLLEGE_SELECT
	)
