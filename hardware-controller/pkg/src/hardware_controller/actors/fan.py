from threading import Event
from typing import Any, override

import gpiod
import paho.mqtt.client as mqtt
import pwmio
from microcontroller import Pin
from paho.mqtt.properties import Properties
from paho.mqtt.reasoncodes import ReasonCode

from .actor import Actor

GPIO_CHIP_PATH = "/dev/gpiochip0"
FAN_FREQUENCY = 25000
MQTT_TOPIC = "actors/fan"


class Fan(Actor):

    @property
    @override
    def DEVICE_NAME(self) -> str:
        return "Fan"

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
        self.__pwmPin: Pin = self._pins[1]
        self.__targetValue: float = 0.0
        self.__targetValueChanged: Event = Event()
        self.__pwm: pwmio.PWMOut = pwmio.PWMOut(
            pin=self.__pwmPin,
            frequency=FAN_FREQUENCY,
            duty_cycle=0
        )
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
                self._log(f"Changing state to '{(self.__targetValue * 100):.2f}%'.")
                if self.__targetValue > 0:
                    self.__gpioRequest.set_value(
                        line=self.__line,
                        value=gpiod.line.Value.ACTIVE
                    )
                self.__pwm.duty_cycle = int((65535 * self.__targetValue))
                if self.__targetValue == 0:
                    self.__gpioRequest.set_value(
                        line=self.__line,
                        value=gpiod.line.Value.INACTIVE
                    )

    @override
    def _deinit(self) -> None:
        try:
            _ = self._mqttClient.loop_stop()
            self.__pwm.duty_cycle = 0
            self.__gpioRequest.set_value(
                line=self.__line,
                value=gpiod.line.Value.INACTIVE
            )
        finally:
            self.__pwm.deinit()
            self.__gpioRequest.release()

    @override
    def _beforeStop(self) -> None:
        pass

    @override
    def _afterStop(self) -> None:
        pass

    def __onConnect(self, client: mqtt.Client, _userdata: Any, _flags: mqtt.ConnectFlags, reasonCode: ReasonCode, _properties: Properties | None) -> None:  # pyright: ignore[reportExplicitAny, reportAny]
        self._log(f"Connected to MQTT with reason code {reasonCode}")
        _ = client.subscribe(
            topic=MQTT_TOPIC
        )

    def __onMessage(self, _client: mqtt.Client, _userdata: Any, msg: mqtt.MQTTMessage) -> None:  # pyright: ignore[reportExplicitAny, reportAny]
        payload: str = msg.payload.decode(encoding="utf-8")
        try:
            payloadNum: float = float(payload)
            if 0 <= payloadNum <= 1:
                self.__targetValue = payloadNum
                self.__targetValueChanged.set()
            else:
                self._log(f"Received out-of-bounds command: {payload}")
        except ValueError:
            self._log(f"Received invalid command: {payload}")
