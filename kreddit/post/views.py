from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import PostForm
from .models import Post
from django.views import View
from kreddit.kredditor.models import Kredditor
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
        response.update({"form": self.form_class()})
        post = Post.objects.get(id=post_id)
        response.update({"post": post})
        response.update({"comments": post.comment_set.get_queryset()})
        return render(request, "./post/post.html", response)

    def post(self, request, subkreddit, post_id):
        form = self.form_class(request.POST)

        if "upvote" in request.POST:
            print("yeah upvote")
        if "downvote" in request.POST:
            comment = Comment.objects.get(id=request.POST['downvote'])
            print(comment)
            print(request.user.kredditor)
            comment.downvotes.add(request.user.kredditor)
            comment.save()
            print(comment.downvotes.all())
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
