class HomeTheaterFacade:

    def __init__(self, amplifier,
                 tuner,
                 dvdPlayer,
                 cdPlayer,
                 projector,
                 screen,
                 theaterLights,
                 popcornPopper):
        self._amplifier = amplifier
        self._tuner = tuner
        self._dvdPlayer = dvdPlayer
        self._cdPlayer = cdPlayer
        self._projector = projector
        self._screen = screen
        self._theaterLights = theaterLights
        self._popcornPopper = popcornPopper

    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self._popcornPopper.on()
        self._popcornPopper.pop()
        self._theaterLights.dim(10)
        self._screen.down()
        self._projector.on()
        self._projector.wideScreenMode()
        self._amplifier.on()
        self._amplifier.setDvdPlayer(self._dvdPlayer)
        self._amplifier.setSurroundSound()
        self._amplifier.setVolume(5)
        self._dvdPlayer.on()
        self._dvdPlayer.play(movie)

    def endMovie(self, movie):
        print("Shutting movie theater down...")
        self._popcornPopper.off()
        self._theaterLights.on()
        self._screen.up()
        self._projector.off()
        self._amplifier.off()
        self._dvdPlayer.stop(movie)
        self._dvdPlayer.eject()
        self._dvdPlayer.off()
