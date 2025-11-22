class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        """Initialize a new song with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment count and update class-level tracking
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total count of songs."""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to genres list if not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Update the genre count histogram."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Update the artist count histogram."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage:
if __name__ == "__main__":
    # Create some songs
    ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
    print(f"Name: {ninety_nine_problems.name}")
    print(f"Artist: {ninety_nine_problems.artist}")
    print(f"Genre: {ninety_nine_problems.genre}")
    
    # Create more songs
    halo = Song("Halo", "Beyonce", "Pop")
    crazy_in_love = Song("Crazy in Love", "Beyonce", "Pop")
    hotline_bling = Song("Hotline Bling", "Drake", "Rap")
    empire_state = Song("Empire State of Mind", "Jay-Z", "Rap")
    
    # Test class methods
    print(f"\nTotal song count: {Song.count}")
    print(f"All artists: {Song.artists}")
    print(f"All genres: {Song.genres}")
    print(f"Genre count: {Song.genre_count}")
    print(f"Artist count: {Song.artist_count}")