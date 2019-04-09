from django.db import models
from kreddit.kredditor.models import Kredditor
from kreddit.subkreddit.models import SubKreddit


class Post(models.Model):
    user = models.ForeignKey(Kredditor, on_delete=models.CASCADE, null=True)
    subkreddit = models.ForeignKey(
        SubKreddit, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200)
    # upvotes = models.ManyToManyField(Kredditor, on_delete=models.CASCADE)
