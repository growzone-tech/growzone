from threading import Event
from typing import Any, override

import gpiod
import paho.mqtt.client as mqtt

from .actor import Actor

GPIO_CHIP_PATH = "/dev/gpiochip0"
MQTT_TOPIC = "actors/lamp"


class Lamp(Actor):

    @property
    @override
    def DEVICE_NAME(self) -> str:
        return "Lamp"

    @override
    def _beforeStart(self) -> None:
        self._mqttClient.on_connect = self.__onConnect
        self._mqttClient.on_message = self.__onMessage

    @override
    def _afterStart(self) -> None:
        pass

    @override
    def _init(self) -> None:
        self.__line: int = self._pins[0].id  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
        self.__targetValue: bool = False
        self.__targetValueChanged: Event = Event()
        chip: gpiod.chip.Chip = gpiod.Chip(path=GPIO_CHIP_PATH)
        self.__gpioRequest: gpiod.line_request.LineRequest = chip.request_lines(
            consumer=self._clientId,
            config={
                self.__line: gpiod.LineSettings(  # pyright: ignore[reportUnknownMemberType]
                    active_low=True,
                    direction=gpiod.line.Direction.OUTPUT,
                    output_value=gpiod.line.Value.INACTIVE
                )
            },
        )
        chip.close()
        _ = self._mqttClient.loop_start()

    @override
    def _run(self) -> None:
        self._log("Monitoring for change requests.")
        while not self._terminate.is_set():
            if self.__targetValueChanged.wait(timeout=5.0):
                self.__targetValueChanged.clear()
                self._log(f"Changing state to '{'On' if self.__targetValue else 'Off'}'.")
                self.__gpioRequest.set_value(
                    line=self.__line,
                    value=gpiod.line.Value.ACTIVE if self.__targetValue else gpiod.line.Value.INACTIVE
                )

    @override
    def _deinit(self) -> None:
        try:
            _ = self._mqttClient.loop_stop()
            self.__gpioRequest.set_value(
                line=self.__line,
                value=gpiod.line.Value.INACTIVE
            )
        finally:
            self.__gpioRequest.release()

    @override
    def _beforeStop(self) -> None:
        pass

    @override
    def _afterStop(self) -> None:
        pass

    def __onConnect(self, client: mqtt.Client, _userdata: Any, _flags: dict[str, int], resultCode: int) -> None:  # pyright: ignore[reportExplicitAny, reportAny]
        self._log(f"Connected to MQTT with result code {resultCode}")
        _ = client.subscribe(
            topic=MQTT_TOPIC
        )

    def __onMessage(self, _client: mqtt.Client, _userdata: Any, msg: mqtt.MQTTMessage) -> None:  # pyright: ignore[reportExplicitAny, reportAny]
        payload: str = msg.payload.decode(encoding="utf-8")
        if payload.lower() in ("true", "yes", "on", "1"):
            self.__targetValue = True
            self.__targetValueChanged.set()
        elif payload.lower() in ("false", "no", "off", "0"):
            self.__targetValue = False
            self.__targetValueChanged.set()
        else:
            self._log(f"Received invalid command: {payload}")
