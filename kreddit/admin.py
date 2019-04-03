from django.contrib import admin
from .kredditor.models import Kredditor
from .post.models import Post

# class TweetAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at',)


admin.site.register(Kredditor)
admin.site.register(Post)
