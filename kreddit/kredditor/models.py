from django.db import models
from django.contrib.auth.models import User


class Kredditor(models.Model):
    # Stretch goal: bio??
    # How to add avatars?
    # Kreddit score field for total upvotes on posts/comments
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username
