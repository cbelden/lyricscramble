from lyricscramble import LyricScrambler


scrambler = LyricScrambler()
songs = [('drake', 'marvins room'), ('drake', 'all me'), ('drake', 'bull shit song')]

# Create corpus
for song in songs:
    if not scrambler.add_song(song[0], song[1]):
        print "Couldn't find: " + str(song)

# Generate phrases
for i in range(10):
    print 'Phrase: ' + scrambler.get_phrase()
