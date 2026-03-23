from threading import Event

from .actors.fan import Fan
from .actors.lamp import Lamp
from .device import HardwareDevice
from .sensors.dht22 import DHT22

STATIC_CONFIG: dict[type[HardwareDevice], tuple[str, ...]] = {
    # Lamp: ("D22",),
    Fan: ("D27", "D12"),
    DHT22: ("D26",)
}


class Main:
    def __init__(self) -> None:
        self.__terminate: Event = Event()
        self.__devices: list[HardwareDevice] = []

    def main(self) -> None:
        for deviceClass, args in STATIC_CONFIG.items():
            self.__devices.append(deviceClass(*args))
        for device in self.__devices:
            device.start()
        while any(map(lambda device: device.isRunning(), self.__devices)):
            if self.__terminate.wait(timeout=1.0):
                break
        for device in self.__devices:
            if device.isRunning():
                device.stop()


def main() -> None:
    main = Main()
    main.main()
