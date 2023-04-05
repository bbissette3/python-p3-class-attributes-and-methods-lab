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
        self.increase_song_count()
        self.add_genre(genre)
        self.add_artist(artist)
        self.increase_genre_count(genre)
        self.increase_artist_count(artist)

    @classmethod
    def increase_song_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def increase_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def increase_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[artist] = 1

