from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from music_app.models import UserProfile, Video, Playlist


def home(request):
	playlists= Playlist.objects.all()[:10]
	return render(request, 'home.html', {'playlist':playlists})


def video(request, video_id):
	video = Video.objects.filter(id=video_id)
	print(video)
	return render(request, 'video.html', {'video': video})

def playlist_page(request, playlist_id):
	playlist = Playlist.objects.filter(id=playlist_id)[0]
	videos = Video.objects.filter(playlist=playlist)
	print(videos)
	return render(request, 'playlist_page.html', {'playlist':playlist, 'videos': videos})