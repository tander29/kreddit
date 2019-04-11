"""kreddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import homepage, login_view, logout_link, kredditor, handler4xx, handler5xx
from .kredditor.urls import urlpatterns as kredditorurls
from .post.urls import urlpatterns as posturls
from .subkreddit.urls import urlpatterns as subkredditurls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_link),
    path('kredditor/<int:user_id>', kredditor)
]

handler404 = handler4xx
handler500 = handler5xx

urlpatterns += kredditorurls
urlpatterns += posturls
urlpatterns += subkredditurls
