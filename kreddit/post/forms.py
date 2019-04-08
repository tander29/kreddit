from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(max_length=500)
