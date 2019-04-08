from django.urls import path
from kreddit.post.views import MyPost

urlpatterns = [
    path('newpost/', MyPost.as_view(), name='newpost')
]
