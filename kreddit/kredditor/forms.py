from django import forms


class Register(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())