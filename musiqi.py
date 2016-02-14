#!/bin/env python

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

new_songs_lyrics = Song(["Babam evlenir 90 yashinda",
			"Guul badam"])

happy_bday.sing_me_a_song()
print('\n')
bulls_on_parade.sing_me_a_song()
print('\n')
new_songs_lyrics.sing_me_a_song()
