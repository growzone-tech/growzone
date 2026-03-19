from typing import override

import adafruit_dht
from microcontroller import Pin

from .sensor import Sensor


class DHT22(Sensor):

    @override
    def _beforeStart(self) -> None:
        pass

    @override
    def _afterStart(self) -> None:
        pass

    @override
    def _init(self) -> None:
        self.__pin: Pin = self._pins[0]
        self.__pinLabel: str = self._pinLabels[0]
        self.__dht22: adafruit_dht.DHT22 = adafruit_dht.DHT22(pin=self.__pin)

    @override
    def _run(self) -> None:
        while not self._terminate.is_set():
            try:
                temperature: int | float | None = self.__dht22.temperature
                if temperature is not None:
                    _ = self._mqttClient.publish(
                        topic="sensor/dht22/inside/temperature",
                        payload=f"{temperature:.2f}",
                        retain=True
                    )
            except RuntimeError as error:
                print(f"Failed reading temperature from DHT22 at GPIO {self.__pinLabel}: {error.args[0]}")
            try:
                humidity: int | float | None = self.__dht22.humidity
                if humidity is not None:
                    _ = self._mqttClient.publish(
                        topic="sensor/dht22/inside/humidity",
                        payload=f"{humidity:.2f}",
                        retain=True
                    )
            except RuntimeError as error:
                print(f"Failed reading humidity from DHT22 at GPIO {self.__pinLabel}: {error.args[0]}")
            _ = self._terminate.wait(timeout=10.0)

    @override
    def _deinit(self) -> None:
        self.__dht22.exit()

    @override
    def _beforeStop(self) -> None:
        pass

    @override
    def _afterStop(self) -> None:
        pass
