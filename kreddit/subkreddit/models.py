from django.db import models
from kreddit.kredditor.models import Kredditor
from django.core.validators import RegexValidator


class SubKreddit(models.Model):
    creator = models.ForeignKey(Kredditor, on_delete=models.CASCADE, null=True, related_name='creator')
    title = models.CharField(max_length=30)
    about = models.CharField(max_length=300)
    rules = models.CharField(max_length=300)
    subscribers = models.ManyToManyField(Kredditor, related_name='subscribers', symmetrical=False, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
