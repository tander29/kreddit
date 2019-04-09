from django.urls import path
from kreddit.post.views import MyPost, PostView

urlpatterns = [
    path('newpost/', MyPost.as_view(), name='newpost'),
    path('subkreddit/<subkreddit>/<post_id>/', PostView.as_view(), name='post')
]
