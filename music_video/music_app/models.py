from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	bio = models.CharField(max_length=264)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

class Category(models.Model):
	genre = models.CharField(max_length=264)

class Comment(models.Model):
	profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	text = models.CharField(max_length=264)
	date = models.DateField(auto_now=True)

class Playlist(models.Model):
	playlist_id = models.CharField(max_length=264, unique=True)
	title = models.CharField(max_length=264)
	description = models.CharField(max_length=2000)
	thumbnail_url= models.CharField(max_length=264)

class Video(models.Model):
	video_id = models.CharField(max_length=264)
	title = models.CharField(max_length=264)
	playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, default='')