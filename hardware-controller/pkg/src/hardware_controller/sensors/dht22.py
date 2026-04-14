from typing import override

import adafruit_dht

from .sensor import Sensor

MQTT_TOPIC_TEMPERATURE = "v1/sensors/dht22/inside/temperature"
MQTT_TOPIC_HUMIDITY = "v1/sensors/dht22/inside/humidity"


class DHT22(Sensor):

    @property
    @override
    def DEVICE_NAME(self) -> str:
        return "DHT22"

    @override
    def _beforeStart(self) -> None:
        pass

    @override
    def _afterStart(self) -> None:
        pass

    @override
    def _init(self) -> None:
        self.__dht22: adafruit_dht.DHT22 = adafruit_dht.DHT22(pin=self._pins[0])

    @override
    def _run(self) -> None:
        self._log(f"Beginning to read data.")
        while not self._terminate.is_set():
            try:
                temperature: int | float | None = self.__dht22.temperature
                if temperature is not None:
                    _ = self._mqttClient.publish(
                        topic=MQTT_TOPIC_TEMPERATURE,
                        payload=f"{temperature:.2f}",
                        retain=True
                    )
            except RuntimeError as error:
                self._log(f"Failed reading temperature: {error.args[0]}")
            try:
                humidity: int | float | None = self.__dht22.humidity
                if humidity is not None:
                    _ = self._mqttClient.publish(
                        topic=MQTT_TOPIC_HUMIDITY,
                        payload=f"{humidity:.2f}",
                        retain=True
                    )
            except RuntimeError as error:
                self._log(f"Failed reading humidity: {error.args[0]}")
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
