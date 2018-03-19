from django import forms
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

class StudentProfile(forms.Form):
    contact=forms.IntegerField(
        required=True,
        label='Contact details'
      

        )
    interest=forms.CharField(
        widget=forms.Textarea,
        max_length=1000,
        label='Enter areas of interest separed by comma'
        )

    gpa=forms.IntegerField(
        required=True,
        label='Enter cgpa'
        )
    income=forms.IntegerField(
        required=True,
        label='Income'
        )
    scores=forms.IntegerField(
        required=True,
        label='Enter SAT score or GRE score')