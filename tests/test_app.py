from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums_paragraphs(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"
    ])
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Released: 1989",
        "Released: 1988", 
        "Released: 1974",
        "Released: 1980",
        "Released: 1990",
        "Released: 2019",
        "Released: 2020",
        "Released: 1965",
        "Released: 1978",
        "Released: 1971",
        "Released: 1982",
        "Released: 1973"
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
Test to confirm we can get to a single artist page
"""

def test_route_to_artist_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists/3")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Genre: Pop",
        "Albums:",
        "Lover",
        "Folklore"
    ])
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Artist: Taylor Swift")


"""
Test to check that get artists contains link to each artist page
"""

def test_get_artists_with_artist_page_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click('text=ABBA')
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Artist: ABBA")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Genre: Pop",
        "Albums:",
        "Waterloo",
        "Super Trouper",
        "Ring Ring"
    ])