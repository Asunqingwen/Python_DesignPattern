from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class MacroCommand(Command):
    def __init__(self, commands):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        for command in self._commands:
            command.undo()
