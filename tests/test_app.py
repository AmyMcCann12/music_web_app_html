from playwright.sync_api import Page, expect

#### Albums Tests

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text(["Doolittle","Surfer Rosa","Waterloo",
        "Super Trouper","Bossanova", "Lover","Folklore","I Put a Spell on You",
        "Baltimore","Here Comes the Sun","Fodder on My Wings","Ring Ring"
    ])
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text(["Released: 1989","Released: 1988", "Released: 1974",
        "Released: 1980","Released: 1990","Released: 2019","Released: 2020","Released: 1965",
        "Released: 1978","Released: 1971","Released: 1982","Released: 1973"
    ])

def test_get_album_via_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Super Trouper")

    album_title_element = page.locator("h1")
    expect(album_title_element).to_have_text("Album: Super Trouper")

    content = page.locator("p")
    expect(content).to_have_text([
        "Release year: 1980",
        "Artist: ABBA"])

def test_get_one_album_2(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/2")
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Release year: 1988")
    artist_tag = page.locator(".t-artist")
    expect(artist_tag).to_have_text("Artist: Pixies")
    heading1_tags = page.locator("h1")
    expect(heading1_tags).to_have_text("Album: Surfer Rosa")\
    
def test_get_one_album_4(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/4")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Release year: 1980",
        "Artist: ABBA"
    ])
    heading1_tags = page.locator("h1")
    expect(heading1_tags).to_have_text("Album: Super Trouper")

"""
Check that we can return to albums page from specific album
"""
def test_return_to_albums_page(page, test_web_address,db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click('text=Waterloo')
    page.click('text=Return to Albums')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text('Albums')

"""
Create a new Album
"""
def test_create_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click('text=Add new album')

    page.fill("input[name='title']", "Test Album")
    page.fill("input[name='release_year']", '1979')
    page.fill("input[name='artist_id']", '3')
    
    page.click("text=Create Album")

    album_title_element = page.locator("h1")
    expect(album_title_element).to_have_text("Album: Test Album")

    content = page.locator("p")
    expect(content).to_have_text([
        "Release year: 1979",
        "Artist: Taylor Swift"])
    
    page.click('text=Return to Albums')
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text(["Doolittle","Surfer Rosa","Waterloo",
        "Super Trouper","Bossanova","Lover","Folklore",
        "I Put a Spell on You","Baltimore","Here Comes the Sun",
        "Fodder on My Wings","Ring Ring","Test Album"
    ])

"""
If we create a new album without a title, release year or artist id
We see an error message
"""
def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text=Add new album')
    page.click('text=Create Album')
    errors = page.locator('.t-errors')
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release year can't be blank, Artist id can't be blank")

def test_create_album_page_shows_artists_and_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/new")
    artists_ids_tag = page.locator(".t-artists-ids")
    expect(artists_ids_tag).to_have_text([
        "Pixies: 1",
        "ABBA: 2",
        "Taylor Swift: 3",
        "Nina Simone: 4"
    ])

### Artists Tests

"""
Test to confirm we can get to a single artist page
"""
def test_get_one_artist_3(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists/3")

    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Pop")

    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Artist: Taylor Swift")

    album_list = page.locator("li")
    expect(album_list).to_have_text([
        "Lover",
        "Folklore"
    ])

"""
Test to check that get artists contains link to each artist page
"""
def test_get_artist_via_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click('text=ABBA')
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Artist: ABBA")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Pop")
    album_list = page.locator("li")
    expect(album_list).to_have_text([
        "Waterloo",
        "Super Trouper",
        "Ring Ring"
    ])

"""
Check that we can return to artists page from specific artist
"""
def test_return_to_artists_page(page, test_web_address,db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click('text=Pixies')
    page.click('text=Return to Artists')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text('Artists')

"""
Test to check creating a new artist 
using a form adds artist to artists list page
"""

def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click('text=Add new artist')

    page.fill("input[name='name']", "Test Artist")
    page.fill("input[name='genre']", "Test Genre")

    page.click("text=Create Artist")

    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Artist: Test Artist")

    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Test Genre")

    album_list = page.locator("li")
    expect(album_list).to_have_text([])

    page.click('text=Return to Artists')
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone" ,"Test Artist"
    ])

"""
If we create a new artist without a name or genre
We see an error message
"""
def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text=Add new artist')
    page.click('text=Create Artist')
    errors = page.locator('.t-errors')
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Genre can't be blank")