class Amplifier:
    def on(self):
        print("Top-O-Line Amplifier on")

    def setDvdPlayer(self, dvdPlayer):
        print("Top-O-Line Amplifier setting DVD player to Top-O-Line DVD Player")

    def setSurroundSound(self):
        print("Top-O-Line Amplifier surround on (5 speakers,1 subwoofer)")

    def setVolume(self, volume):
        print("Top-O-Line Amplifier setting volume to" + volume.__str__())

    def off(self):
        print("Top-O-Line Amplifier off")


class CDPlayer:
    pass


class DVDPlayer:
    def on(self):
        print("Top-O-Line DVD Player on")

    def play(self, movie):
        print("Top-O-Line DVD Player playing" + movie)

    def stop(self, movie):
        print("Top-O-Line DVD Player stopped" + movie)

    def eject(self):
        print("Top-O-Line DVD Player eject")

    def off(self):
        print("Top-O-Line DVD Player off")


class PopcornPopper:
    def on(self):
        print("Popcorn Popper on!")

    def pop(self):
        print("Popcorn Popper popping popcorn!")

    def off(self):
        print("Popcorn Popper off!")


class Projector:
    def on(self):
        print("Top-O-Line Projector on")

    def off(self):
        print("Top-O-Line Projector off!")

    def wideScreenMode(self):
        print("Top-O-Line Projector in widescreen mode (16x9 aspect ratio)")


class Screen:
    def down(self):
        print("Theater Screen going down!")

    def up(self):
        print("Theater Screen going up!")


class TheaterLights:
    def dim(self, dim):
        print("Theater Ceiling Lights dimming to " + dim.__str__() + "%")

    def on(self):
        print("Theater Ceiling Lights on!")


class Tuner:
    pass
