from Devices import Amplifier, Tuner, DVDPlayer, CDPlayer, Projector, TheaterLights, Screen, PopcornPopper
from Facade import HomeTheaterFacade

if __name__ == '__main__':
    amplifier = Amplifier()
    tuner = Tuner()
    dvdPlayer = DVDPlayer()
    cdPlayer = CDPlayer()
    projector = Projector()
    theaterLights = TheaterLights()
    screen = Screen()
    popcornPopper = PopcornPopper()

    homeTheaterFacade = HomeTheaterFacade(amplifier, tuner, dvdPlayer, cdPlayer,
                                          projector, screen, theaterLights, popcornPopper)

    homeTheaterFacade.watchMovie("Raiders of the Lost Ark")
    homeTheaterFacade.endMovie("Raiders of the Lost Ark")
