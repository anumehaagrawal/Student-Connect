from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import College, Counsellor, User
from datetime import datetime
from django.utils import timezone

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user

class CounsellorSignUpForm(UserCreationForm):
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
    UNI_SELECT = [(col.title, col.title) for col in College.objects.order_by('title')]
   
    #phone_number = forms.IntegerField(required=True)
    email = forms.CharField(required=True)
    phone_number=forms.CharField(required=False)
    university = forms.ChoiceField(required=True, choices=UNI_SELECT)
    sat_score = forms.CharField(required=False)
    act_score = forms.CharField(required=False)
    gpa = forms.CharField(required=False)
    ethnicity = forms.ChoiceField(required=False, choices=ETHNIC_SELECT)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_counsellor = True
        user.save()

        counsellor = Counsellor(
            user=user,
            email=self.data['email'],
            last_login=timezone.now(),
            phone_number=self.data['phone_number'],
            university=self.data['university'],
            sat_score=self.data['sat_score'],
            act_score=self.data['act_score'],
            gpa=self.data['gpa'],
            ethnicity=self.data['ethnicity'],
        )
        counsellor.save()

        return counsellor
