from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Login
from .post.models import Post
from .subkreddit.models import SubKreddit
from .subkreddit.helper import sort_posts, toggle_post_upvotes
from .kredditor.models import Kredditor, User


@login_required()
def homepage(request):
    response = {}
    subscribed = SubKreddit.objects.filter(
        subscribers=request.user.kredditor.id)
    # initializes posts as empty query
    posts = Post.objects.none()
    subkreddit_list = []
    for subkreddit in subscribed:
        find_posts = Post.objects.filter(subkreddit=subkreddit).all()
        posts = posts | find_posts
        subkreddit_list.append(subkreddit.title)
    response.update({'posts': sort_posts(posts),
                     "subscribed": subkreddit_list})

    if request.method == 'POST':
        toggle_post_upvotes(request)
        return HttpResponseRedirect(reverse("homepage"))
    return render(request, 'homepage.html', response)


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
    user = User.objects.get(pk=user_id)
    posts = sort_posts(Post.objects.filter(user=user.kredditor))
    created_subs = SubKreddit.objects.filter(creator=user.kredditor)
    subs_list = []

    for sub in created_subs:
        subs_list.append(sub.title)

    if request.method == 'POST':
        toggle_post_upvotes(request)
        return HttpResponseRedirect(reverse("kredditor",
                                            kwargs={'user_id': user_id}))

    return render(request, 'kredditor/profile.html',
                  {'user': user,
                   'posts': posts,
                   "subscribed": subs_list})


def handler4xx(request, *args, **kwargs):
    return render(request, 'errorhandling/404.html', status=404)


def handler5xx(request, *args, **kwargs):
    return render(request, 'errorhandling/500.html', status=500)
