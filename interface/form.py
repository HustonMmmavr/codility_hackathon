from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from interface.models import Profile, FakeCard
from django.core.files import File
from django import forms
import urllib

class LoginForm(forms.Form):
    login = forms.CharField(
            widget=forms.TextInput(
                attrs={ 'class': 'form-control', 'placeholder': 'login', 'autocomplete' : 'off'}
                ),
            max_length=30,
            label=u'Login'
            )

    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={ 'class': 'form-control', 'type': 'password', 'placeholder': 'password', 'autocomplete' : 'off'}),
            label=u'Password'
            )

    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data.get('login', ''), password=data.get('password', ''))
        if user is not None:
            if user.is_active:
                data['user'] = user
            else:
                raise forms.ValidationError(u'This user don\'t active')
        else:
            raise forms.ValidationError(u'Uncorrect login or password')


class SignupForm(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': 'Login', }),
            max_length=30, label=u'Login'
            )
    first_name = forms.CharField(
            widget=forms.TextInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': u'Ivan', }),
            max_length=30, label=u'Name'
            )
    last_name = forms.CharField(
            widget=forms.TextInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': u'Ivanov', }),
            max_length=30, label=u'Second name'
            )
    email = forms.EmailField(
            widget=forms.TextInput( attrs={ 'class': 'form-control inp-radius', 'type': 'email', 'placeholder': u'ivanov@gmail.com', }),
            required = True, max_length=254, label=u'E-mail'
            )
    password1 = forms.CharField(
            widget=forms.PasswordInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': u'*****' }),
            min_length=6, label=u'Password'
            )
    password2 = forms.CharField(
            widget=forms.PasswordInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': u'*****' }),
            min_length=6, label=u'Repeat password'
            )

        

    interest = forms.CharField(
            widget=forms.TextInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': u'...', }),
            required=False, label=u'Interests'
            )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        try:
            u = User.objects.get(username=username)
            print('a')
            raise forms.ValidationError(u'User exist')
        except User.DoesNotExist:
            print('b')
            return username

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1', '')
        pass2 = self.cleaned_data.get('password2', '')

        if pass1 != pass2:
            raise forms.ValidationError(u'Passwords not equal')

    def save(self):
        data = self.cleaned_data
        password = data.get('password1')
        user = User()

        user.username = data.get('username')
        user.password = make_password(password)
        user.email = data.get('email')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.is_active = True
        user.is_superuser = False
       
        user.save()
        

        profile = Profile()
        fake_card = FakeCard()
        fake_card.save()

        profile.user = user
        profile.interest = data.get('interest')
        profile.fake_card = fake_card
        profile.save()
        
        return authenticate(username=user.username, password=password)

class DonateForm(forms.Form):
    cash = forms.CharField(
            widget=forms.TextInput( attrs={ 'class': 'form-control inp-radius', 'placeholder': 'Login', }),
            max_length=30, label=u'donate'
            )

    def clean(self):
        data = self.cleaned_data
        cashChar = data.get('cash', '')
        try:
            cash = int(cashChar)
            if (cash < 0):
                raise ValidationError(u'Cant donate < 0')
        except ValueError:
            raise ValidationError(u'Please input integer data')
            

