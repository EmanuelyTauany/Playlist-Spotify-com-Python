import sys
import spotipy
import spotipy.util as util

artistasFile = open('artistas.txt', 'r')
artista = [x.strip('\n') for x in artistasFile.readlines()]

tracks=[]

numeroArtistas = len(artista)



username='Emanuely Tauany'
scope='playlist-modify-public'
playlist_id='5wKVxTN4N9yiVYsGbwC0C4'

token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id ='      ',
                                   client_secret='     ',
                                   redirect_uri='http://localhost:8080/callback')
if token:
    sp= spotipy.Spotify(auth=token)
    sp.trace = False

    for x in range(0, numeroArtistas):
        result = sp.search(artista[x], limit=4)
        for i, t in enumerate(result['tracks']['items']):
            tracks.append(str(t['id'].strip('u')))
            print("adicionando a track", t['id'], t['name'])
    
    while tracks:
        try:
            result = sp.user_playlist_add_tracks(username, playlist_id, tracks[:1])
        except Exception as e:
            print("erro", e)
        tracks= tracks[1:]
    #print(len(tracks))
    
    #print(results)

else:
    print("Can't get token for", username)