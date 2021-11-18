from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter the password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter the password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm the password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'
