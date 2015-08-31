# -- coding: utf-8 --
from django import forms
from .models import Account  # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()

        return user

class ChangeInfoFrom(forms.Form):
    #CHOICES = [('男', '1'),
    #           ('女', '0')]
    #sexRadios = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    username = forms.CharField(required=True)
    school = forms.CharField()
    whatsup = forms.CharField()

    class Meta:
        model = Account
        fields = ('username', 'school', 'whatsup')

    def save(self, commit=True):
        user = super(ChangeInfoFrom, self).save(commit=False)
        #user.sex = self.cleaned_data['sex']
        user.username = self.cleaned_data['username']
        user.school = self.cleaned_data['school']
        user.whatsup = self.cleaned_data['whatsup']

        if commit:
            user.save()

        return user

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ChangePassForm(forms.Form):
    pass
