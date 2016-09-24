from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album, Song, Image, Video
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, SongForm
from django.http import HttpResponse
import os
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        albums = Album.objects.all()
        image = Image.objects.all()
        video = Video.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()

            image = image.filter(
                Q(image_title__icontains=query)
            ).distinct()

            video = video.filter(
                Q(video_title__icontains=query)
            ).distinct()

            return render(request, 'music/search.html', {
                'albums': albums,
                'image': image,
                'video': video,
            })
        else:
            return render(request, 'music/index.html', {'albums': albums})

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        song = form.save(commit=False)
        song.album = album
        song.save()
        return render(request, 'music/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)

class SongUpdate(UpdateView):
    model = Song
    fields = ['song_title', 'song_file']

def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank from
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.all()
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def images(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        image = Image.objects.all()

        return render(request, 'music/images.html', {
            'image': image,
            })


class ImagesCreate(CreateView):
    model = Image
    fields = ['image_title', 'image_file']

class ImagesUpdate(UpdateView):
    model = Image
    fields = ['image_title', 'image_file']

class ImagesDelete(DeleteView):
    model = Image
    success_url = reverse_lazy('music:images')


def videos(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        video = Video.objects.all()

        return render(request, 'music/videos.html', {
            'video': video,
            })

class VideosCreate(CreateView):
    model = Video
    fields = ['video_title', 'video_file']

class VideosUpdate(UpdateView):
    model = Video
    fields = ['video_title', 'video_file']

class VideosDelete(DeleteView):
    model = Video
    success_url = reverse_lazy('music:videos')



















