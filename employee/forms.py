from django import forms

class LoginForm(forms.Form):
    User_Name = forms.CharField(max_length = 100, widget = forms.TextInput())
    Password =  forms.CharField(max_length = 50, widget = forms.PasswordInput())
