from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'input',
        'name': 'input',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'name': 'password',
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'input',
        'name': 'input',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'name': 'password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password1',
        'name': 'password1',
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password1')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'mobile',
        'class': 'data_special',
        'readonly': True,
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'name',
        'class': 'data_special',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
        'class': 'data_special',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'address',
        'class': 'data_special',
    }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'last_name')