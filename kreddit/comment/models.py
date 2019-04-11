from django.db import models
from kreddit.kredditor.models import Kredditor
from kreddit.post.models import Post
import datetime
import pytz
from pytz import timezone


class Comment(models.Model):
    user = models.ForeignKey(Kredditor, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(
        Kredditor, related_name="commentupvotes", blank=True)
    downvotes = models.ManyToManyField(
        Kredditor, related_name="commentdownvotes", blank=True)

    def get_score(self):
        return self.upvotes.count() - self.downvotes.count()

    # stretch goal: have value that determines order to appear based on time and score i.e every hour create hidden score=score-time that has passed
    def hidden(self):
        eastern = timezone('US/Eastern')
        current_time = eastern.localize(datetime.datetime.now())
        # a = eastern.localize(current_time)
        difference = current_time - self.date_created
        datetime.timedelta(0, 8, 562000)
        return divmod(difference.days * 86400 + difference.seconds, 60)

        # return current_time

        # return datetime.datetime.now(timezone.America/Indiana/Indianapolis)
        # print(dir(timezone))
