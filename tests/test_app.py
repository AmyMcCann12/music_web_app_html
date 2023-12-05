from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Title: Doolittle",
        "Released: 1989",
        "Title: Surfer Rosa",
        "Released: 1988", 
        "Title: Waterloo",
        "Released: 1974",
        "Title: Super Trouper",
        "Released: 1980",
        "Title: Bossanova",
        "Released: 1990",
        "Title: Lover",
        "Released: 2019",
        "Title: Folklore",
        "Released: 2020",
        "Title: I Put a Spell on You",
        "Released: 1965",
        "Title: Baltimore",
        "Released: 1978",
        "Title: Here Comes the Sun",
        "Released: 1971",
        "Title: Fodder on My Wings",
        "Released: 1982",
        "Title: Ring Ring",
        "Released: 1973"
    ])

def test_get_one_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/2")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Release year: 1988",
        "Artist: Pixies"
    ])
    heading1_tags = page.locator("h1")
    expect(heading1_tags).to_have_text("Surfer Rosa")