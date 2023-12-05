from lib.album import Album

class AlbumRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row['id'],row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums
    
    def find(self, album_id):
        rows = self.connection.execute('SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
        return album
    
    def create(self, album):
        self.connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None
    
    def delete(self, album_id):
        self.connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id]
        )
        return None
    
    def find_with_artist(self, album_id):
        rows = self.connection.execute(
            """SELECT albums.id AS album_id, 
            albums.title, 
            albums.release_year, 
            albums.artist_id, 
            artists.name 
            FROM albums JOIN artists ON artists.id = albums.artist_id 
            WHERE albums.id = %s""",
            [album_id]
        )
        row = rows[0]
        album = Album(row['album_id'], row['title'], row['release_year'], row['artist_id'], row['name'])
        print(album)
        return album