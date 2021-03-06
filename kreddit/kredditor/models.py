from django.db import models
from django.contrib.auth.models import User


class Kredditor(models.Model):
    # How to add avatars?
    # Kreddit score field for total upvotes on posts/comments
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
