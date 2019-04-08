from django.urls import path
from kreddit.subkreddit.views import AllSubs

urlpatterns = [
    path('allsubs/', AllSubs.as_view(), name='allsubs')
]
