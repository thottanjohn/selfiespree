from django.conf.urls import url,include
from django.contrib import admin
from . import views
app_name="contest"

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add$', views.EntryCreate.as_view(), name='addentry'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^page/(?P<user_id>[0-9]+)/$', views.page, name='pages'),
    url(r'^page/$', views.detail, name='detail'),    


]

                        
 