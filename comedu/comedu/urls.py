"""comedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from comedu_calendar.views import *

from customuser.views import mainView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    ##add for calendar
    url(r'^calendar/', include('comedu_calendar.urls', namespace = 'calendar')),
    url(r'^search/$', calendar_search),
=======

    # polls app url
    url(r'^polls/', include('polls.urls')),

    # main page
    url(r'^$', mainView, name='home'),
>>>>>>> 966c616d984e30c2d01e30bb34155714c5fc133e
]
