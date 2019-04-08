from django import forms


class NewSubkredditForm(forms.Form):
    title = forms.CharField(max_length=30)
    about = forms.CharField(max_length=300)
    rules = forms.CharField(max_length=300)
