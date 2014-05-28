from lyricscramble import LyricScrambler


songs = {'Mumford and sons': ['the cave', 'hopeless wanderer', 'little lion man']}
s = LyricScrambler(songs)

for i in range(10):
    print s.get_phrase()
    print ''
