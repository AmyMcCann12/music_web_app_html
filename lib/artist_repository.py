from lib.artist import Artist
from lib.album import Album

class ArtistRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self.connection = connection

    # Retrieve all artists
    def all(self):
        rows = self.connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by their id
    def find(self, artist_id):
        rows = self.connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    def find_with_albums(self, artist_id):
        albums = []
        rows = self.connection.execute(
            """SELECT albums.id AS album_id,
            albums.title, albums.release_year, albums.artist_id,
            artists.id,
            artists.name,
            artists.genre
            FROM artists 
            JOIN albums 
            ON albums.artist_id = artists.id 
            WHERE artists.id = %s""",
            [artist_id])
        print(rows)
        for row in rows:
            album = Album(row['album_id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(album)
        rows = self.connection.execute('SELECT * FROM artists WHERE id = %s', [artist_id]) 
        artist = Artist(rows[0]['id'], rows[0]['name'], rows[0]['genre'], albums)
        return artist
    
    def create(self, artist):
        rows = self.connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        row = rows[0]
        artist.id = row["id"]
        return None

    def delete(self, artist_id):
        self.connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None
