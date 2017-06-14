####################USES TSWIFT PACKAGE BY BRENNS10 ON GITHUB#####################
#note: relies on user for capitalization due to unusual caps in artist names
import terminal
terminal.run_bash('pip3 install tswift', True)
from tswift import *

def known_music(artist, song_title):
    song = Song(title=song_title, artist=artist)
    return song.format()

def query_handler(command):
    relevant = command[command.index("lyrics")+6:]
    relevant = relevant.strip()
    artist = relevant[relevant.index("by") + 2:].strip()
    song = relevant[0:relevant.index("by")].strip()
    try:
        return known_music(artist, song) + "\n"
    except KeyError:
        return "That song isn't in the database :/"
