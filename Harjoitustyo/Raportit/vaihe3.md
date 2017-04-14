Yritetääs hakea soittolista spotifysta.

## rekisteröinti
https://developer.spotify.com/
https://developer.spotify.com/web-api/

remove from this, store elsewhere
id: ae827a8dfc2b4081bfd120816e948ebc
secret: ff111fff4e6f42249955dd8450887641

## sivun lisääminen
linkki
playlist.html
reititys

https://open.spotify.com/user/1168568460/playlist/2cFuJk1eQIhp66xd1WoCFV

@app.route('/playlist', methods=['GET'])
def playlist():
    # insert API-calls here!
    return render_template('playlist.html')

## spotify API
hmm
https://spotipy.readthedocs.io/en/latest/
pip install spotipy

https://github.com/plamere/spotipy/blob/master/examples/user_playlists_contents.py
