import spotipy
import spotipy.util as util

username = 'ayberkDeneme'
scope = 'user-library-read'
scope = 'playlist-modify-public'

CLIENT_ID = 'bcc57908a2e54cee94f9e2307db67c2e'
CLIENT_SECRET = '6831b3ceaf0a40a6a1fdeb67105ef19b'

playlist_id = '57hQnYeBC4u0IUhaaHmM0k'

token = util.prompt_for_user_token(username, 
                                   scope,
                                   client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   redirect_uri='https://open.spotify.com')

sp = spotipy.Spotify(auth=token)