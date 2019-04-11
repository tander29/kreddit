from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import PostForm
from .models import Post
from .helper import toggle_comment_upvotes, sort_comments
from django.views import View
from kreddit.comment.forms import CommentForm
from kreddit.comment.models import Comment
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
    form_class = CommentForm

    def get(self, request, subkreddit, post_id):
        response = {}
        post = Post.objects.get(id=post_id)
        comments = sort_comments(post.comment_set.get_queryset())

        response.update({"post": post})
        response.update({"form": self.form_class()})
        response.update(
            {"comments": comments})
        return render(request, "./post/post.html", response)

    def post(self, request, subkreddit, post_id):
        form = self.form_class(request.POST)
        toggle_comment_upvotes(request)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                body=data['body'],
                user=request.user.kredditor,
                post=Post.objects.get(id=post_id)
            )
        return HttpResponseRedirect(reverse('post',
                                            kwargs={"subkreddit": subkreddit,
                                                    "post_id": post_id}))
