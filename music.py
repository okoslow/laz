#pip3 install tswift -> run_bash

####################USES TSWIFT PACKAGE BY BRENNS10 ON GITHUB#####################
from tswift import *

def known_music(artist, song_title):
    song = Song(title=song_title, artist=artist)
    return song.format()
#
# tswift 'Lynyrd Skynyrd' -s Freebird -> get freebird song lyrics
# lyric search mode tswift -l 'I would walk 500 miles'

# print(Song.find_song(lyrics)
