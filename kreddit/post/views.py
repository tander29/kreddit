from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import PostForm
from django.views import View


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
