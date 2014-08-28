from django import forms
from IMGGaming.models import Report
from IMGGaming.models import UserProfile
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):
    event = forms.CharField(max_length=100)
    author = forms.CharField(max_length=40)
    datetime = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY HH:MM'}))
    diagnosis = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 140, 'style': 'width: 100%'}))
    impact = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%'}))
    resolution  = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%'}))
    responsibility = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%'}))
    actionable = forms.BooleanField(required=False)
    action = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%'}))

    class Meta:
        model = Report
	widgets = {
            'datetime' : forms.DateInput(attrs={'class':'date'})
        }

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)
    
    class Meta:
        model = UserProfile
        fields = ('picture',)
