from django.urls import path
from kreddit.subkreddit.views import AllSubsView, SubKredditView

urlpatterns = [
    path('subkreddit/', AllSubsView.as_view(), name='subkreddits'),
    path('subkreddit/<subkreddit>', SubKredditView.as_view(), name='subkreddit')
]
