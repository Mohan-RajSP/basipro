from django import forms
from django.core.exceptions import ValidationError
from basiapp.models import UserProfileInfo
from django.contrib.auth.models import User

class Userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(),label="Password")

    class Meta():
        model = User
        fields = ('username','email','password')

class Portfolio(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','portfolio')






