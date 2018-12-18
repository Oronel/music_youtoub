from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from music_app.models import UserProfile, Video, Playlist


def home(request):
	use = request.user
	users = UserProfile.objects.all()
	playlist= Playlist.objects.all()[:10]
	videos = Video.objects.all().order_by('-date')
	return render(request, 'home.html', {'playlist':playlist, 'users': users, 'videos': videos})
