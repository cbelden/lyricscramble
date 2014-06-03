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
        self.chain_is_current = False

    def _get_lyrics(self, artist, title):
        """Retrieves the full lyric listing (if available) for the given song."""

        # Retrieve song lyrics
        client = LyricClient()
        return client.get_lyrics(artist, title)

    def add_song(self, artist, title):
        """Adds a song to the current corpus. Returns False if song is not found."""

        # Get lyrics
        lyrics = self._get_lyrics(artist, title)

        # Return False; song was not found.
        if not lyrics:
            return False

        # Make sure corpus size isn't maxed out. Pop oldest song.
        if len(self._corpus) >= self._max_songs:
            del self._corpus[0]

        # Add song to corpus
        self._corpus.append(Song(artist, title, lyrics))
        self._chain_is_current = False
        return True

    def update_chain(self):
        """Creates a Markov chain based on the current corpus."""

        text_corpus = ''
        for song in self._corpus:
            text_corpus += song.lyrics

        if not text_corpus:
            raise Exception("Error: no corpus to generate MarkovChain")

        self._chain = MarkovChain(text_corpus)
        self.chain_is_current = True

    def get_phrase(self, max_size=None, min_words=None):
        """Generates a silly phrase based on the underlying Markov Chain."""

        if not self._chain:
            raise Exception('No Markov chain instance to generate a phrase.')

        return self._chain.generate_phrase(max_size=max_size, min_words=min_words)
