import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_video.settings')
import django
django.setup()
from music_app.models import Playlist, Video


api_key='AIzaSyD_1-MMYnetxD_gFNSlv_VStHOf1dDpSsQ'
channel_id='UCupvZG-5ko_eiXAupbDfxWw'
playlists_api_url = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&key={}&maxResults={}'.format(channel_id ,api_key, 30)
# https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UCupvZG-5ko_eiXAupbDfxWw&key=AIzaSyD_1-MMYnetxD_gFNSlv_VStHOf1dDpSsQ&maxResults=30

def get_videos(playlist):
	print('Aaaaaaaaaaaaa')		
	playlist_id_test = playlist.playlist_id
	playlist_api_url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=20&playlistId={}&key={}'.format(playlist_id_test, api_key)
	print(playlist_api_url)
	videos_json = requests.get(playlist_api_url).json()
	for play in videos_json["items"]:
		video = Video.objects.get_or_create(video_id=play['snippet']['resourceId']['videoId'], title=play['snippet']['title'] , playlist=playlist)[0]


def get_playlists(playlists_api_url):
	playlist_json = requests.get(playlists_api_url).json()
	print(playlists_api_url)
	for item in playlist_json['items']:
		print('#########')
		playlist = Playlist.objects.get_or_create(playlist_id= item['id'], title=item['snippet']['title'],
			description=item['snippet']['description'],thumbnail_url=item['snippet']['thumbnails']['high']['url'])[0]
		print(playlist)
		get_videos(playlist)	


if __name__ == '__main__':
  print('Starting to populate...')
  get_playlists(playlists_api_url)
  print('Finished populating!') 