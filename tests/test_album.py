from lib.album import *

"""
Album constructs with an id, title, release year, and artist id
"""

def test_album_constructs_with_given_properties():
    album = Album(1, "Title name", "Year of Release", 2)
    assert album.id == 1
    assert album.title == "Title name"
    assert album.release_year == "Year of Release"
    assert album.artist_id == 2

"""
When we compare two identical albums, 
they are classed as equal
"""

def test_two_identical_albums():
    album1 = (1, "Title", "Release", 2)
    album2 = (1, "Title", "Release", 2)
    assert album1 == album2

"""
We can format albums to strings nicely
"""

def test_format_album_nicely():
    album1 = Album(1, "Title", "Release", 2)
    assert str(album1) == "Album(1, Title, Release, 2)"
