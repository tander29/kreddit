from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Login


@login_required()
def homepage(request):
    return render(request, 'homepage.html')


def login_view(request):
    form = None

    if request.method == 'POST':
        form = Login(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user is not None:
                login(request, user)

                return HttpResponseRedirect(request.GET.get('next', '/'))

    else:
        form = Login()

    return render(request, 'login_form.html', {'form': form})


def logout_link(request):
    logout(request)

    return HttpResponseRedirect(request.GET.get('next', '/'))
