from kreddit.comment.models import Comment


def toggle_comment_upvotes(request):
    if "upvote" in request.POST:
        print("yeah upvote")
        comment = Comment.objects.get(id=request.POST['upvote'])
        if request.user.kredditor in comment.upvotes.all():
            comment.upvotes.remove(request.user.kredditor)
        else:
            comment.downvotes.remove(request.user.kredditor)
            comment.upvotes.add(request.user.kredditor)
        print(comment.upvotes.all())
    if "downvote" in request.POST:
        comment = Comment.objects.get(id=request.POST['downvote'])
        if request.user.kredditor in comment.downvotes.all():
            comment.downvotes.remove(request.user.kredditor)
        else:
            comment.upvotes.remove(request.user.kredditor)
            comment.downvotes.add(request.user.kredditor)
        comment.save()
        print(comment.downvotes.all())
    return
