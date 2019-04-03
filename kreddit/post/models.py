from django.db import models
from kreddit.kredditor.models import Kredditor


class Post(models.Model):
    # image?
    # upvotes
    user = models.ForeignKey(Kredditor, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
