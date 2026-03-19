import abc
import os
from threading import Event, Thread

import board
import microcontroller
import paho.mqtt.client as mqtt
from microcontroller import Pin

MQTT_HOST: str = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT: int = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_TIMEOUT = 60


class HardwareDevice(metaclass=abc.ABCMeta):

    def __init__(self, *pinLabels: str) -> None:
        self._pins: tuple[microcontroller.Pin, ...] = tuple[Pin, ...](map[Pin](self.__resolvePinLabel, pinLabels))
        self._pinLabels: tuple[str, ...] = pinLabels
        self.__thread: Thread = Thread(target=self.run)
        self._terminate: Event = Event()
        self.__running: bool = False
        self._mqttClient: mqtt.Client = mqtt.Client(
            client_id=f"Hardware_Device__{'_'.join(pinLabels)}",
            protocol=mqtt.MQTTv5
        )

    def __resolvePinLabel(self, pinLabel: str) -> microcontroller.Pin:
        if hasattr(board, pinLabel):
            pin = getattr(board, pinLabel)  # pyright: ignore[reportAny]
            if not isinstance(pin, microcontroller.Pin):
                raise ValueError(f"Pin with label '{pinLabel}' is not of type 'microcontroller.Pin'.")
        else:
            raise ValueError(f"Pin with label '{pinLabel}' not found on this board!")
        return pin

    def start(self) -> None:
        self._beforeStart()
        self.__thread.start()
        self._afterStart()

    def run(self) -> None:
        self.__running = True
        try:
            _ = self._mqttClient.connect(
                host=MQTT_HOST,
                port=MQTT_PORT,
                keepalive=MQTT_TIMEOUT
            )
            self._init()
            self._run()
        finally:
            try:
                self._deinit()
            finally:
                _ = self._mqttClient.disconnect()
                self.__running = False

    def stop(self) -> None:
        self._beforeStop()
        self._terminate.set()
        self.__thread.join()
        self._afterStop()

    def isRunning(self) -> bool:
        return self.__running

    @abc.abstractmethod
    def _beforeStart(self) -> None:
        pass

    @abc.abstractmethod
    def _afterStart(self) -> None:
        pass

    @abc.abstractmethod
    def _init(self) -> None:
        pass

    @abc.abstractmethod
    def _run(self) -> None:
        pass

    @abc.abstractmethod
    def _deinit(self) -> None:
        pass

    @abc.abstractmethod
    def _beforeStop(self) -> None:
        pass

    @abc.abstractmethod
    def _afterStop(self) -> None:
        pass
