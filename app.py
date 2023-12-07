import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/albums/<id>')
def get_single_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find_with_artist(id)
    # artist_repository = ArtistRepository(connection)
    # artist_name = artist_repository.find(album.artist_id).name
    return render_template('albums/album.html', album=album)

# GET albums/new
# Returns a form to create a new album
@app.route('/albums/new', methods = ['GET'])
def get_new_album():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('albums/new.html', artists = artists)

# POST /albums
# Creates a new album
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    new_album = Album(None, title, release_year, artist_id)
    
    if not new_album.is_valid():
        return render_template('albums/new.html', album=new_album, errors=new_album.generate_errors()), 400

    repository.create(new_album)
    return redirect(f"/albums/{new_album.id}")

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists = artists)

@app.route('/artists/<id>')
def get_single_arist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find_with_albums(id)
    return render_template('artists/artist.html', artist = artist)

@app.route('/artists/new', methods = ['GET'])
def get_new_artist():
    return render_template('artists/new.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    
    name = request.form['name']
    genre = request.form['genre']
    print(name, genre)

    new_artist = Artist(None, name, genre)
    
    if not new_artist.is_valid():
        return render_template('artists/new.html', album=new_artist, errors=new_artist.generate_errors()), 400

    repository.create(new_artist)
    return redirect(f"/artists/{new_artist.id}")

@app.route('/artists/delete/<int:id>',  methods = ['GET'])
def delete_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.delete(id)
    return redirect(f"/artists")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

