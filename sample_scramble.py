from lyricscramble import LyricScrambler


songs = {'Mumford and sons': ['the cave', 'hopeless wanderer', 'little lion man', 'bogus song']}
s = LyricScrambler(songs)

print 'Missing songs: ' + str(s.missing_songs)

for i in range(10):
    print 'Phrase: ' + s.get_phrase()
