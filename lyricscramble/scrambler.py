from lyricfetch import LyricClient
from markovchain import MarkovChain


class Song():
    """Container class for song information."""

    def __init__(self, artist, title, lyrics):
        """Instantiates the Song object."""
        self.artist = artist
        self.title = title
        self.lyrics = lyrics


class LyricScrambler():
    """Generates scrambled phrases based on song lyrics."""

    def __init__(self):
        """Initializes the LyricScrambler."""

        # Set max corpus size (# songs)
        self._max_songs = 10

        # Initialize the corpus and Markov chain
        self._corpus = []
        self._chain = {}

        # Signifies if current Markov chain reflects the corpus
        self._chain_is_current = False

    def _get_lyrics(self, artist, title):
        """Retrieves the full lyric listing (if available) for the given song."""

        # Retrieve song lyrics
        client = LyricClient()
        return client.get_lyrics(artist, title)

    def add_song(self, artist, title):
        """Adds a song to the current corpus. Returns False if song is not found."""

        # Type check
        artist_valid = artist and type(artist) is str
        title_valid = title and type(title) is str

        if not artist_valid or not title_valid:
            raise ValueError("Expected string input for artist and title.")

        # Get lyrics
        lyrics = self._get_lyrics(artist, title)

        # Return False; song was not found.
        if not lyrics:
            return False

        # Make sure corpus size isn't maxed out. Pop oldest song.
        if len(self._corpus) >= self._max_songs:
            del self._corpus[0]

        # Add song to corpus; note that the Markov chain is not current
        self._corpus.append(Song(artist, title, lyrics))
        self._chain_is_current = False
        return True

    def _update_chain(self):
        """Creates a Markov chain based on the current corpus."""

        text_corpus = ''
        for song in self._corpus:
            text_corpus += song.lyrics

        if not text_corpus:
            raise Exception("Error: no corpus to generate MarkovChain")

        # Create a new Markov chain, and signal that it is current
        self._chain = MarkovChain(text_corpus)
        self._chain_is_current = True

    def get_phrase(self, max_size=None, min_words=None):
        """Generates a silly phrase based on the underlying Markov Chain."""

        # Ensure there's corpus
        if not self._corpus:
            raise Exception('No song lyrics to generate a phrase.')

        # Update the Markov chain
        if not self._chain_is_current:
            self._update_chain()

        # _chain.generate_phrase will raise a ValueError if max_size and min_words
        # are invalid.
        return self._chain.generate_phrase(max_size=max_size, min_words=min_words)
