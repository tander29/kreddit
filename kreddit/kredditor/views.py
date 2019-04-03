from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Kredditor
from .forms import Register


def register(request):
    form = None

    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['first_name'],
                data['last_name'],
                data['username'],
                data['email'],
                data['password']
            )

            login(request, user)

            Kredditor.objects.create(
                user=user
            )

            return HttpResponseRedirect(reverse('homepage.html'))

    form = Register()

    return render(request, 'kredditor/register_form.html', {'form': form})
