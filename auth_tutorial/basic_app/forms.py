from django import forms
from django.contrib.auth.models import User
from basic_app.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('portfolio_site', 'profile_pic')
