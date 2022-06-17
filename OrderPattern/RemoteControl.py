from OrderPattern.Command import NoCommand


class RemoteControl:
    def __init__(self):
        self._onCommands = list()
        self._offCommands = list()
        self._noCommand = NoCommand()
        self._undoCommand = self._noCommand
        for _ in range(7):
            self._onCommands.append(self._noCommand)
            self._offCommands.append(self._noCommand)

    def setCommand(self, slot, onCommand, offCommand):
        self._onCommands[slot] = onCommand
        self._offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self._onCommands[slot].execute()
        self._undoCommand = self._onCommands[slot]

    def offButtonWasPushed(self, slot):
        self._offCommands[slot].execute()
        self._undoCommand = self._offCommands[slot]

    def undoButtonWasPushed(self):
        self._undoCommand.undo()

    def toString(self):
        stringBuffer = ""
        stringBuffer += "\n------ Remote Control -------\n"
        for i in range(len(self._onCommands)):
            stringBuffer += "[slot " + i.__str__() + "] " + self._onCommands[i].__class__.__name__ + "    " + \
                            self._offCommands[
                                i].__class__.__name__ + "\n"
        stringBuffer += "[undo] " + self._undoCommand.__class__.__name__ + "\n"
        return stringBuffer
