from django.conf.urls import url
from django.contrib import admin

from . import views
app_name="music"
urlpatterns = [

        url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='music_detail'),
        url(r'^$',views.IndexView.as_view(),name='index'),
        url(r'^album/add$',views.AlbumCreate.as_view(),name='album-add'),
        url(r'^album/(?P<pk>[0-9]+)$',views.AlbumUpdate.as_view(),name='album-update'),
        url(r'^album/(?P<pk>[0-9]+)/delete$',views.AlbumDelete.as_view(),name='album-delete'),
        url(r'^nav$',views.nav.as_view(),name='nav'),
        url(r'^login$',views.UserFormView.as_view(),name='login'),
]
                        
 