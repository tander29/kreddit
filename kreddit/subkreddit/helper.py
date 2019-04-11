from kreddit.post.models import Post
from kreddit.subkreddit.models import SubKreddit


def toggle_post_upvotes(request):
    if "upvote" in request.POST:
        print("yeah upvote")
        post = Post.objects.get(id=request.POST['upvote'])
        if request.user.kredditor in post.upvotes.all():
            post.upvotes.remove(request.user.kredditor)
        else:
            post.downvotes.remove(request.user.kredditor)
            post.upvotes.add(request.user.kredditor)
        print(post.upvotes.all())
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
    if "unsubscribed" in request.POST:
        sub_k = SubKreddit.objects.get(id=request.POST["unsubscribe"])
        sub_k.subscribers.remove(current_user)
        sub_k.save()
