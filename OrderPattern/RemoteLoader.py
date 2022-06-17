from OrderPattern.Command import LightOnCommand, LightOffCommand
from OrderPattern.Devices import Light
from OrderPattern.RemoteControl import RemoteControl

if __name__ == '__main__':
    remoteControl = RemoteControl()

    livingRoomLight = Light("Living Room")
    kitchenLight = Light("Kitchen")

    livingRoomLightOn = LightOnCommand(livingRoomLight)
    livingRoomLightOff = LightOffCommand(livingRoomLight)
    kitchenLightOn = LightOnCommand(kitchenLight)
    kitchenLightOff = LightOffCommand(kitchenLight)

    remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
    remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff)
    print(remoteControl.toString())

    remoteControl.onButtonWasPushed(0)
    remoteControl.offButtonWasPushed(0)
    print(remoteControl.toString())
    remoteControl.undoButtonWasPushed()

    remoteControl.onButtonWasPushed(1)
    remoteControl.offButtonWasPushed(1)
    remoteControl.undoButtonWasPushed()
