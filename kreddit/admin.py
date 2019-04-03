from django.contrib import admin
from .kredditor.models import Kredditor


# class TweetAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at',)


admin.site.register(Kredditor)
