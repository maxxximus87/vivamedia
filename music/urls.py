from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/ homepage
    url(r'^$', views.index, name='index'),

    #/login_user
    url(r'^login_user/$', views.login_user, name='login_user'),

    #/music/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/logout
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /music/album_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album-update"),

    #/music/album/2/delete
     url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album-delete"),

    #/music/song/add/
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    #/music/song/2/
    url(r'^song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name="song-update"),

    #/music/song/2/delete
     url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

    #/music/images/
     url(r'^images/$', views.images, name='images'),

    #/music/album/add/
    url(r'images/add/$', views.ImagesCreate.as_view(), name='images-add'),

    #/music/song/2/
    url(r'^images/(?P<pk>[0-9]+)/$', views.ImagesUpdate.as_view(), name="images-update"),

    #/music/song/2/delete
     url(r'^images/(?P<pk>[0-9]+)/delete/$', views.ImagesDelete.as_view(), name="delete_images"),

     #/music/images/
     url(r'^videos/$', views.videos, name='videos'),

    #/music/album/add/
    url(r'videos/add/$', views.VideosCreate.as_view(), name='videos-add'),

    #/music/song/2/
    url(r'^videos/(?P<pk>[0-9]+)/$', views.VideosUpdate.as_view(), name="videos-update"),

    #/music/song/2/delete
     url(r'^videos/(?P<pk>[0-9]+)/delete/$', views.VideosDelete.as_view(), name="delete_videos"),

]
