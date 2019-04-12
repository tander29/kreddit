from kreddit.post.models import Post
from kreddit.subkreddit.models import SubKreddit


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
    return


def subscriber_check(request, sub):
    print(sub.subscribers.get_queryset().all())
    if request.user.kredditor in sub.subscribers.get_queryset().all():
        return True
    else:
        return False


def toggle_subscribe(request):
    current_user = request.user.kredditor
    if "subscribe" in request.POST:
        sub_k = SubKreddit.objects.get(id=request.POST["subscribe"])
        sub_k.subscribers.add(current_user)
        sub_k.save()
    if "unsubscribe" in request.POST:
        sub_k = SubKreddit.objects.get(id=request.POST["unsubscribe"])
        sub_k.subscribers.remove(current_user)
        sub_k.save()
    return


def sort_posts(posts):
    sorted_posts = sorted(posts, reverse=True,
                          key=lambda post: post.get_score())
    return sorted_posts
