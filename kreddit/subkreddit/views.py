from django.views import View
from django.shortcuts import render, reverse, HttpResponseRedirect


class AllSubs(View):
    def get(self, request):
        response = {}
        allsubs = [1, 2, 3]
        response.update({'allsubs': allsubs})
        return render(request, "./subkreddit/allsubs.html", response)
