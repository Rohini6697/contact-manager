from django import forms
from django.contrib.auth.models import User

from . import Contacts



class UserRegistrationForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.NumberInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email']

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
            Contacts.objects.create(
                name = user.username,
                email = user.email,
                number = user.phone,
                role = self.cleaned_data['phone']
            )