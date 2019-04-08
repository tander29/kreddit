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
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                email=data['email'],
                password=data['password']
            )

            login(request, user)

            Kredditor.objects.create(
                user=user
            )

            return HttpResponseRedirect(reverse('homepage'))

    form = Register()

    return render(request, 'kredditor/register_form.html', {'form': form})
