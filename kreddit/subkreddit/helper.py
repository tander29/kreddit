from kreddit.post.models import Post


def toggle_post_upvotes(request):
    if "upvote" in request.POST:
        post = Post.objects.get(id=request.POST['upvote'])
        if request.user.kredditor in post.upvotes.all():
            post.upvotes.remove(request.user.kredditor)
        else:
            post.downvotes.remove(request.user.kredditor)
            post.upvotes.add(request.user.kredditor)
        post.save()
    if "downvote" in request.POST:
        post = Post.objects.get(id=request.POST['downvote'])
        if request.user.kredditor in post.downvotes.all():
            post.downvotes.remove(request.user.kredditor)
        else:
            post.upvotes.remove(request.user.kredditor)
            post.downvotes.add(request.user.kredditor)
        post.save()
        print(post.downvotes.all())
    return
