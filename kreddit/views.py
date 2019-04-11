from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Login
from .post.models import Post


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


def kredditor(request, user_id):
    posts = Post.objects.filter(id=user_id)

    return render(request, 'kredditor/profile.html', {'user': request.user, 'posts': posts})


def handler4xx(request, *args, **kwargs):
    return render(request, 'errorhandling/404.html', status=404)


def handler5xx(request, *args, **kwargs):
    return render(request, 'errorhandling/500.html', status=500)
