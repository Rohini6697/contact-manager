from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import AuthenticationForm

from .models import Contacts



class UserRegistrationForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.NumberInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('confirm_password'):
            raise forms.ValidationError('Password is not matching')
        return data
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit :
            user.save()
            
        return user
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))