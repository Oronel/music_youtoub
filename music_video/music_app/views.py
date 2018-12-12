from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from music_app.models import UserProfile, Video


def home(request):
	use = request.user
	user = UserProfile.objects.get(user=use)
	users = UserProfile.objects.all()
	videos = Video.objects.all().order_by('-date')
	return render(request, 'home.html', {'profile':user, 'users': users, 'videos': videos})
