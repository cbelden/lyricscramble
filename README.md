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

Now, install the lyricscramble and the dependencies I've written (copy and paste starting at 'pip'):

    (venv)JaneDoe$ pip install git+git://github.com/cbelden/markovchain.git@master git+git://github.com/cbelden/lyricfetch.git@master git+git://github.com/cbelden/lyricscramble.git@master

See the Use section below on how to use lyricscramble!

##Use
If you're continuing from the Installation section, you can go ahead start a python session
and do the lyricscramble demo (shown below).

Make sure (in Terminal) you're in the directory where you created the virtual environment and
make sure it's activated. Then, start the python interpreter and give lyricscramble a try:

    (venv)JaneDoe$ python
    >>> from lyricscramble import LyricScrambler
    >>> songs = {'Mumford and Sons': ['little lion man']}
    >>> scrambler = LyricScrambler(songs)
    >>> print scrambler.get_phrase()
    This is an example phrase that might be output

And there you have it! You can now create non-sensical phrases based on your favorite songs. And
remember, virtual environment sessions can be deactivated with the command 'deactivate:'

    (venv)JaneDoe$ deactivate
