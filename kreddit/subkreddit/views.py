from django.views import View
from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import NewSubkredditForm
from .models import SubKreddit
from kreddit.post.forms import PostForm
from kreddit.post.models import Post
from kreddit.kredditor.models import Kredditor
from .helper import toggle_post_upvotes, toggle_subscribe, subscriber_check, sort_posts
<<<<<<< HEAD
# from selenium import webdriver
=======
>>>>>>> e955e510bf57fa279c377aa3b3c2f853991ae838


class AllSubsView(View):
    form_class = NewSubkredditForm

    def get(self, request):
        response = {}
        form = self.form_class()
        response.update({"form": form})
        allsubs = SubKreddit.objects.all()
        response.update({'allsubs': allsubs})
        return render(request, "./subkreddit/allsubs.html", response)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() and hasattr(request.user, 'kredditor'):
            data = form.cleaned_data
            SubKreddit.objects.create(
                creator=request.user.kredditor,
                title=data['title'].replace(" ", ""),
                about=data['about'],
                rules=data['rules']
            )
            return HttpResponseRedirect(reverse("subkreddits"))
        form = self.form_class()
        return render(request, "./subkreddit/allsubs.html", {"form": form})


class SubKredditView(View):
    form_class = PostForm

    def get(self, request, subkreddit):
        response = {}
        form = self.form_class()
        html = "./subkreddit/subkreddit.html"
        sub = SubKreddit.objects.filter(title=subkreddit).first()
        posts = sort_posts(Post.objects.filter(subkreddit=sub).all())
        response.update({"sub": sub, "form": form,
                         "posts": posts, "validsub": bool(sub),
                         "is_subbed": subscriber_check(request, sub),
                         "validuser": hasattr(request.user, 'kredditor')})
        return render(request, html, response)

    def post(self, request, subkreddit):
        form = self.form_class(request.POST)
        toggle_post_upvotes(request)
        toggle_subscribe(request)
        if form.is_valid():
            data = form.cleaned_data
            user = Kredditor.objects.get(pk=request.user.kredditor.pk)
            # driver = webdriver.PhantomJS()
            # driver.get(data['url'])
            # driver.save_screenshot(data['title'] + '.png')
            Post.objects.create(
                user=user,
                title=data['title'],
                body=data['body'],
                url=data['url'],
                subkreddit=SubKreddit.objects.filter(title=subkreddit).first()
            )
        return HttpResponseRedirect(reverse('subkreddit',
                                            kwargs={"subkreddit": subkreddit}))
