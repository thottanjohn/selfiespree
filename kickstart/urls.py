"""kickstart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from selfiecontest import views as views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^about/$',views.about,name="about"),
	url(r'^polls/', include('polls.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^contest/',include('contest.urls')),    
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^add$', views.EntryCreate.as_view(), name='addentry'),
    url(r'^page/(?P<image_id>[0-9]+)/$', views.page, name='pages'),
    url(r'^page/$', views.detail, name='detail'),
    url(r'^events/$', views.events, name='events'),    
    url(r'^profile$', views.view_profile, name='profile'),
    url(r'^profile/edit$', views.update_profile, name='edit_profile'),
    url(r'^about/$', views.about, name='about'),
    url(r'^bas/$', views.bas, name='bas'),

   
]

if settings.DEBUG:
        urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
        urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
