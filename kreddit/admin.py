from django.contrib import admin
from .kredditor.models import Kredditor
from .post.models import Post
from .comment.models import Comment
from .message.models import Message
from .subkreddit.models import SubKreddit


# class TweetAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at',)


admin.site.register(Kredditor)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(SubKreddit)
