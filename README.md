#lyricscramble

##About
The lyricscramble package generates silly phrases based on lyrics from user-specified songs.

##Installation (Mac OS X)
The following instructions describe how to install the lyricscramble package using a
virtual environment. If you're unfamiliar with virtual environments for Python, there
is plenty of documentation online.

First, open a new terminal and navigate to the directory where you'll want to use lyricscramble. Then,
create and activate a new virtual environment:

    JaneDoe$ virtualenv venv
    JaneDoe$ source venv/bin/activate

Now install a few of the dependencies (Some other python packages I've written. In the future,
I would like to add these to PyPI to automate the dependency installation.). The lyricfetch package
retrieves lyrics from the Lyric Wikia website, and the markovchain package generates a markov
chain (bigram language model) based on text input.

    (venv)JaneDoe$ pip install git+git://github.com/cbelden/lyricfetch.git@master
    (venv)JaneDow$ pip install git+git://github.com/cbelden/markovchain.git@master

Now, install the lyricscramble package:

    (venv)JaneDoe$ pip install git_git://github.com/cbelden/lyricscramble.git@master

##Use
To ensure you've installed lyricscramble correctly, start a python terminal session in the same
directory where you created the virtual environment (and make sure it's activated):

    (venv)JaneDoe$ python
    >>> from lyricscramble import LyricScrambler
    >>> songs = {'Mumford and Sons': ['little lion man']}
    >>> scrambler = LyricScrambler(songs)
    >>> print scrambler.get_phrase()
    This is an example phrase that might be output

And there you have it! You can now create non-sensical phrases based on your favorite songs.
