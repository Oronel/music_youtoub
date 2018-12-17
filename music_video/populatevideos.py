import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_video.settings')
import django
django.setup()
from music_app.models import Playlist, Video



api_key='AIzaSyD_1-MMYnetxD_gFNSlv_VStHOf1dDpSsQ'
channel_id='UCPVhZsC2od1xjGhgEc2NEPQ'
playlists_api_url = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(api_key, channel_id, 20)


def get_videos(playlist):
	play_id = playlist[0].playlist_id
	playlist_api_url='https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={}&playlistId={}&key={}'.format(20, play_id, api_key)
	videos_json = requests.get(playlist_api_url).json()
	for play in videos_json["items"]:
		video = Video.objects.get_or_create(video_id=play['id'], title=play['snippet']['title'] , playlist=playlist[0])[0]



def get_playlists(playlists_api_url):
	playlist_json = requests.get(playlists_api_url).json()
	for item in playlist_json['items']:
		print(item)
		if 'playlistId' in item['id']:
			playlist = Playlist.objects.get_or_create(playlist_id= item['id']['playlistId'], title=item['snippet']['title'],
				description=item['snippet']['description'],thumbnail_url=item['snippet']['thumbnails']['default']['url'])
			print(playlist)
			get_videos(playlist)
			
		


if __name__ == '__main__':
  print('Starting to populate...')
  get_playlists(playlists_api_url)
  print('Finished populating!') 