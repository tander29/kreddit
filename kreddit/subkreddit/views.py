from django.views import View
from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import NewSubkredditForm
from .models import SubKreddit
from kreddit.post.forms import PostForm
from kreddit.post.models import Post


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
                title=data['title'].replace(" ", ""),
                about=data['about'],
                rules=data['rules'],
                user=request.user.kredditor
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
        posts = Post.objects.filter(subkreddit=sub).all()
        response.update({"sub": sub, "form": form,
                         "posts": posts, "validsub": bool(sub),
                         "validuser": hasattr(request.user, 'kredditor')})
        return render(request, html, response)

    def post(self, request, subkreddit):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title=data['title'],
                body=data['body'],
                subkreddit=SubKreddit.objects.filter(title=subkreddit).first()
            )
        return HttpResponseRedirect(reverse('subkreddit', kwargs={"subkreddit": subkreddit}))
