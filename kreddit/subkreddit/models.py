from django.db import models
from kreddit.kredditor.models import Kredditor


class SubKreddit(models.Model):
    user = models.ForeignKey(Kredditor, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    about = models.CharField(max_length=300)
    rules = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
