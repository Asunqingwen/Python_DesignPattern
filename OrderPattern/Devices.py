class Light:
    def __init__(self, place):
        self.place = place

    def on(self):
        print(self.place + "'s light is On!")

    def off(self):
        print(self.place + "'s light is Off!")


class Stereo:
    def __init__(self, place):
        self.place = place

    def on(self):
        print(self.place + "'s Stereo is On!!")

    def off(self):
        print(self.place + "'s Stereo is Off!")

    def setCD(self):
        print(self.place + "'s Stereo has set CD!")

    def setDVD(self):
        print(self.place + "'s Stereo has set DVD!")

    def setRadio(self):
        print(self.place + "'s Stereo has set radio!")

    def setVolume(self, volume):
        print(self.place + "'s Stereo's volume is " + volume)


class GarageDoor:
    def __init__(self, place):
        self.place = place

    def up(self):
        print("Garage door is Open!")

    def down(self):
        print("Garage door is Close!")

    def stop(self):
        print("Garage door is Stop!")

    def lightOn(self):
        print("Garage door'light is On!")

    def lightOff(self):
        print("Garage door'light is Off!")


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, place):
        self.place = place
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH

    def medium(self):
        self.speed = self.MEDIUM

    def low(self):
        self.speed = self.LOW

    def off(self):
        self.speed = self.OFF

    def getSpeed(self):
        return self.speed
