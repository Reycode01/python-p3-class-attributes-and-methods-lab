class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        Song.count += 1

        # Add the genre to the genres list if not already present
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Add the artist to the artists list if not already present
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Increment the genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Increment the artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
