import os
import threading
from threading import Event

import board
import gpiod
import pwmio

from .device import HardwareDevice
from .sensors.dht22 import DHT22

GPIO_CHIP_PATH = "/dev/gpiochip0"
GPIO_PIN_LIGHT = int(os.environ.get("GPIO_PIN_LIGHT", "22"))
GPIO_PIN_FAN = int(os.environ.get("GPIO_PIN_FAN", "27"))
GPIO_PIN_FAN_PWM = int(os.environ.get("GPIO_PIN_FAN_PWM", "12"))
GPIO_PIN_DHT = int(os.environ.get("GPIO_PIN_DHT", "26"))
FAN_FREQUENCY = 25000

STATIC_CONFIG: dict[type[HardwareDevice], tuple[str]] = {
    # "Light": (22,),
    # "Fan": (27, 12),
    DHT22: ("D26",)
}


class Main:
    def __init__(self) -> None:
        self.__terminate: Event = threading.Event()
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
        # self.test_lamp()
        # self.test_fan()

    def test_lamp(self) -> None:
        with gpiod.request_lines(
            GPIO_CHIP_PATH,
            consumer="light-test",
            config={
                GPIO_PIN_LIGHT: gpiod.LineSettings(
                    active_low=True,
                    direction=gpiod.line.Direction.OUTPUT,
                    output_value=gpiod.line.Value.INACTIVE
                )
            },
        ) as request:
            print("Turning on light.")
            request.set_value(GPIO_PIN_LIGHT, gpiod.line.Value.ACTIVE)
            _ = self.__terminate.wait(60.0)
            print("Turning off light.")
            request.set_value(GPIO_PIN_LIGHT, gpiod.line.Value.INACTIVE)

    def test_fan(self) -> None:
        with gpiod.request_lines(
            GPIO_CHIP_PATH,
            consumer="fan-test",
            config={
                GPIO_PIN_FAN: gpiod.LineSettings(
                    active_low=True,
                    direction=gpiod.line.Direction.OUTPUT,
                    output_value=gpiod.line.Value.INACTIVE
                )
            },
        ) as request:
            print("Turning on fan.")
            request.set_value(GPIO_PIN_FAN, gpiod.line.Value.ACTIVE)
            pwm = pwmio.PWMOut(getattr(board, f"D{GPIO_PIN_FAN_PWM}"), frequency=FAN_FREQUENCY, duty_cycle=0)  # pyright: ignore[reportAny]
            try:
                for i in range(1, 11):
                    print(f"Fan: {i * 10}%")
                    pwm.duty_cycle = int((65535 * (i / 10)))
                    _ = self.__terminate.wait(6.0)
            finally:
                print("Turning off fan.")
                pwm.duty_cycle = 0
                pwm.deinit()
                request.set_value(GPIO_PIN_FAN, gpiod.line.Value.INACTIVE)


def main() -> None:
    main = Main()
    main.main()
