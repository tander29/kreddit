from kreddit.comment.models import Comment


def toggle_comment_upvotes(request):
    if "upvote" in request.POST:
        comment = Comment.objects.get(id=request.POST['upvote'])
        if request.user.kredditor in comment.upvotes.all():
            comment.upvotes.remove(request.user.kredditor)
        else:
            comment.downvotes.remove(request.user.kredditor)
            comment.upvotes.add(request.user.kredditor)
    if "downvote" in request.POST:
        comment = Comment.objects.get(id=request.POST['downvote'])
        if request.user.kredditor in comment.downvotes.all():
            comment.downvotes.remove(request.user.kredditor)
        else:
            comment.upvotes.remove(request.user.kredditor)
            comment.downvotes.add(request.user.kredditor)
        comment.save()
    return


def sort_comments(comments):
    sorted_comments = sorted(
        comments, reverse=True,
        key=lambda comment: comment.get_score())
    return sorted_comments
