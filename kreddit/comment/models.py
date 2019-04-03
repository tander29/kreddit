from django.db import models
from kreddit.kredditor.models import Kredditor
from kreddit.post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(Kredditor, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
