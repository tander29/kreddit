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
    # url_img = models.ImageField(upload_to='screenshots/')
    upvotes = models.ManyToManyField(
        Kredditor, related_name="upvotes", blank=True)
    downvotes = models.ManyToManyField(
        Kredditor, related_name="downvotes", blank=True)

    def get_score(self):
        return self.upvotes.count() - self.downvotes.count()
