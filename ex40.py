class Song(object):

    def __init__(self, lyrics):
        self.lyrics= lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["happy birth day to you",
                    "I don't want to get sued",
                    "So il'll stop here"])

bulls_in_parade = Song(["THEY RALLY AROUND AMIL",
                        "With pocket full shes"])

happy_bday.sing_me_a_song()

bulls_in_parade.sing_me_a_song()
