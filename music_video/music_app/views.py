from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from music_app.models import UserProfile, Video, Playlist


def home(request):
	playlist= Playlist.objects.all()[:10]
	videos = Video.objects.all()
	return render(request, 'home.html', {'playlist':playlist, 'videos': videos})


def videos(request):
	playlist= Playlist.objects.all()[:10]
	videos = Video.objects.all()[:10]
	return render(request, 'videos.html', {'playlist':playlist,'videos': videos})
