from django import forms
from IMGGaming.models import Report
from IMGGaming.models import UserProfile
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):
    event = forms.CharField(max_length=100)
    author = forms.CharField(max_length=40)
    datetime = forms.DateTimeField()
    diagnosis = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%'}))
    impact = forms.CharField(widget=forms.Textarea(attrs={}))
    resolution  = forms.CharField(widget=forms.Textarea(attrs={}))
    responsibility = forms.CharField(widget=forms.Textarea(attrs={}))
    actionable = forms.BooleanField(required=False)
    action = forms.CharField(widget=forms.Textarea(attrs={}))

    class Meta:
        model = Report

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
