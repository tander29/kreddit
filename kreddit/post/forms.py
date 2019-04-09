from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(max_length=500)
    url = forms.URLField(max_length=200, required=False)
