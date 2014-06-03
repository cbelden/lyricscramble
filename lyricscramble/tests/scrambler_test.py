import unittest
from lyricscramble import LyricScrambler


class TestLyricScrambler(unittest.TestCase):
    """Tests (some of) the methods of the LyricScrambler class."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ~~~~~~~~~~~~~~~ TEST constructor ~~~~~~~~~~~~~~~~

    def test_constructor(self):
        """Tests the LyricScrambler constructor."""
        # Holding off on writing this test; nothing public is
        # exposed after creating the LyricScrambler object. Currently
        # do not accept input parameters.
        pass

    # ~~~~~~~~~~~~~~~ TEST add_song ~~~~~~~~~~~~~~~~

    def test_add_song_valid_input(self):
        """Tests the add_song method."""

        # Choosing a song that Lyric Wikia has the lyrics too
        artist = 'drake'
        title = 'marvins room'

        ls = LyricScrambler()
        successfully_added_song = ls.add_song(artist, title)

        # Assert the method returned True on success
        self.assertTrue(successfully_added_song)

        # Assert that the Markov chain is no longer current
        self.assertFalse(ls._chain_is_current)

        # Assert corpus reflects this change
        new_song = ls._corpus[-1]
        self.assertTrue(artist is new_song.artist)
        self.assertTrue(title is new_song.title)
        self.assertTrue(new_song.lyrics)

    def test_add_song_bogus_title(self):
        """Tests that add_song returns False when a lyrics are not found."""

        # Fictitious song
        artist = 'drake'
        title = 'some bogus song that is not real'

        ls = LyricScrambler()
        successfully_added_song = ls.add_song(artist, title)

        # Assert method returns False on failure
        self.assertFalse(successfully_added_song)

        # Assert corpus is still empty
        self.assertFalse(ls._corpus)

    def test_add_song_invalid_input(self):
        """Tests that add_song raises an error with an invalid (non-string) input."""

        ls = LyricScrambler()

        # Test when artist is invalid
        self.assertRaises(ValueError, ls.add_song, '', 'some song')
        self.assertRaises(ValueError, ls.add_song, 1, 'some song')

        # Test when song is invalid
        self.assertRaises(ValueError, ls.add_song, 'artist', '')
        self.assertRaises(ValueError, ls.add_song, 'artist', 1)

    def test_add_song_to_full_corpus(self):
        """Tests that the add_song method pops the oldest song in the corpus before adding the new song."""

        ls = LyricScrambler()
        ls._max_songs = 1

        # Add legitimate song
        ls.add_song('drake', 'marvins room')

        # Add another legitimate song
        artist = 'mumford and sons'
        title = 'i will wait'
        ls.add_song(artist, title)

        # Make sure corpus is maximum size
        self.assertEqual(len(ls._corpus), ls._max_songs)

        # Make sure corpus song is the most recently added
        self.assertEqual(ls._corpus[-1].title, title)

    # ~~~~~~~~~~~~~~~ TEST _update_chain ~~~~~~~~~~~~~~~~

    def test_update_chain(self):
        """Tests that the _update_chain method updates the underlying Markov chain."""

        ls = LyricScrambler()
        artist = 'drake'
        title = 'marvins room'

        # Add this song to the corpus and assert chain is not current and empty
        ls.add_song(artist, title)
        self.assertFalse(ls._chain_is_current)
        self.assertFalse(ls._chain)

        # Call update chain; ensure chain is updated
        ls._update_chain()
        self.assertTrue(ls._chain_is_current)
        self.assertTrue(ls._chain)

    def test_update_chain_with_no_corpus(self):
        """Tests that the update_chain method fails when there is no corpus."""

        ls = LyricScrambler()
        self.assertRaises(Exception, ls._update_chain)

    # ~~~~~~~~~~~~~~~ TEST get_phrase ~~~~~~~~~~~~~~~~

    def test_get_phrase_no_input(self):
        """Tests that the get_phrase method returns a phrase when there is a corpus and no input parameters."""

        ls = LyricScrambler()
        ls.add_song('drake', 'marvins room')

        phrase = ls.get_phrase()

        # Assert that the underlying chain is current and the return value is a string
        self.assertTrue(ls._chain_is_current)
        self.assertEqual(type(phrase), str)
        self.assertTrue(phrase)

    def test_get_phrase_with_valid_input(self):
        """Tests that the get_phrase method returns the specified phrase with valid input."""

        ls = LyricScrambler()
        artist = 'drake'
        title = 'marvins room'

        ls.add_song(artist, title)
        max_size = 140
        min_words = 5
        phrase = ls.get_phrase(max_size=max_size, min_words=min_words)

        self.assertTrue(len(phrase) < max_size)
        self.assertTrue(len(phrase.split(' ')) >= min_words)

    def test_get_phrase_with_invalid_input(self):
        """Tests that the get_phrase method raises a ValueError when max_size and min_words are invalid."""

        ls = LyricScrambler()
        ls.add_song('drake', 'marvins room')

        # Assert get_phrase raises an error when parameters are incompatible
        self.assertRaises(ValueError, ls.get_phrase, max_size=10, min_words=10)

        # Assert get_phrase raises an error when max_size is invalid
        self.assertRaises(ValueError, ls.get_phrase, max_size=-1)
        self.assertRaises(ValueError, ls.get_phrase, max_size='cheese')

        # Assert get_phrase raises an error when min_words is invalid
        self.assertRaises(ValueError, ls.get_phrase, min_words=-1)
        self.assertRaises(ValueError, ls.get_phrase, min_words='cheese')

        # Assert get_phrase raises an error when both params are invalid
        self.assertRaises(ValueError, ls.get_phrase, max_size='cheese', min_words=-1)


if __name__ == '__main__':

    # Run tests
    unittest.main()
