from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import PostForm
from .models import Post
from django.views import View
from kreddit.kredditor.models import Kredditor

"Post belong to subkreddit, comment belong to post"


class MyPost(View):
    form_class = PostForm

    def get(self, request):
        form = self.form_class()
        return render(request, "./post/newpost.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("register"))
        form = self.form_class()
        return render(request, "./post/newpost.html", {"form": form})


class PostView(View):
    def get(self, request, subkreddit, post_id):
        response = {}
        post = Post.objects.get(id=post_id)
        response.update({"post": post})
        return render(request, "./post/post.html", response)
