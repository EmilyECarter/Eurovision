from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import sys
import os
import spotipy.util as util




scope = 'user-library-read'
credentials = spotipy.oauth2.SpotifyOAuth('3c1d55c596254b63a0cca3f9c99d1221','f527a426fed9453b936ebf3ea39cf4ad', 'localhost:/callback', scope = scope, cache_path = '.spotipyoauthcache')
#sp = spotipy.Spotify(client_credentials_manager=credentials)


auth_url = credentials.get_authorize_url()


code = credentials.parse_response_code(auth_url)

access_token = ""
token_info = credentials.get_access_token(code)
print token_info
access_token = token_info['access_token']

sp = spotipy.Spotify(client_credentials_manager=credentials)

search_str = 'Eurovision 2010-2016'
result = sp.search(q=search_str, type='playlist')
#pprint.pprint(result)


def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

#just set the ID's for the one we now, no need to generalise
playlists = sp.user_playlist('11102203945', playlist_id='S4arUPSyB2dLTFiCvvW1O')
for playlist in playlists['items']:
    print()
    print(playlist['name'])
    print('  total tracks', playlist['tracks']['total'])
    results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
    tracks = results['tracks']
    show_tracks(tracks)
    while tracks['next']:
        tracks = sp.next(tracks)
        show_tracks(tracks)




# shows acoustic features for tracks for the given artist

#from __future__ import print_function    # (at top of module)
#from spotipy.oauth2 import SpotifyClientCredentials
#import json
#import spotipy
#import time
#import sys


#client_credentials_manager = SpotifyClientCredentials()
#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#sp.trace=False

#if len(sys.argv) > 1:
#    artist_name = ' '.join(sys.argv[1:])
#    results = sp.search(q=artist_name, limit=50)
#    tids = []
#    for i, t in enumerate(results['tracks']['items']):
#        print(' ', i, t['name'])
#        tids.append(t['uri'])
    
    #    start = time.time()
    #    features = sp.audio_features(tids)
    #delta = time.time() - start
    #print(json.dumps(features, indent=4))
#print ("features retrieved in %.2f seconds" % (delta,))