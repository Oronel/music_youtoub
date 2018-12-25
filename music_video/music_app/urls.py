from . import views
from django.urls import path

app_name='music_app'

urlpatterns = [
path('home/', views.home, name='home'),
path('playlist_page/<int:playlist_id>', views.playlist_page, name='playlist_page'),
path('video/<int:video_id>', views.video, name='video'),
]