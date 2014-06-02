from lyricfetch import LyricClient
from markovchain import MarkovChain


class LyricScrambler():
    """Generates scrambled phrases based on song lyrics."""

    def __init__(self, songs):
        """Initializes the LyricScrambler."""

        # Will store songs whose lyrics could not be found
        self.missing_songs = []

        # Generate underlying Markov chain
        corpus = self._get_lyrics(songs)
        self._chain = MarkovChain(corpus)

    def _get_lyrics(self, songs):
        """Retrieves the lyrics for each song and returns a concatenated string."""

        lyrics = ''
        client = LyricClient()

        for artist, titles in songs.iteritems():
            for title in titles:

                # Retrieve and append lyrics
                new_lyrics = client.get_lyrics(artist, title)

                # Add to missing songs if no lyrics returned
                if not new_lyrics:
                    self.missing_songs.append((artist, title))

                lyrics += new_lyrics

        return lyrics

    def get_phrase(self):
        """Generates a silly phrase based on the underlying Markov Chain."""

        return self._chain.generate_phrase()
