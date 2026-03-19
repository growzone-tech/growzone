import os
import threading

import adafruit_dht
import board
import gpiod
import paho.mqtt.client as mqtt
import pwmio
import RPi.GPIO

MQTT_HOST = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_TIMEOUT = 60
GPIO_CHIP_PATH = "/dev/gpiochip0"
GPIO_PIN_LIGHT = int(os.environ.get("GPIO_PIN_LIGHT", "22"))
GPIO_PIN_FAN = int(os.environ.get("GPIO_PIN_FAN", "27"))
GPIO_PIN_FAN_PWM = int(os.environ.get("GPIO_PIN_FAN_PWM", "12"))
GPIO_PIN_DHT = int(os.environ.get("GPIO_PIN_DHT", "26"))
FAN_FREQUENCY = 25000


class Main:
    def __init__(self) -> None:
        self.__terminate = threading.Event()
        self.__dht22 = adafruit_dht.DHT22(getattr(board, f"D{GPIO_PIN_DHT}"))
        self.__mqttClient = mqtt.Client(
            protocol=mqtt.MQTTv5
        )

    def connect_mqtt(self) -> None:
        try:
            self.__mqttClient.connect(MQTT_HOST, MQTT_PORT, MQTT_TIMEOUT)
        except Exception as e:
            raise e

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
            self.__terminate.wait(60.0)
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
            pwm = pwmio.PWMOut(getattr(board, f"D{GPIO_PIN_FAN_PWM}"), frequency=FAN_FREQUENCY, duty_cycle=0)
            try:
                for i in range(1, 11):
                    print(f"Fan: {i * 10}%")
                    pwm.duty_cycle = int((65535 * (i / 10)))
                    self.__terminate.wait(6.0)
            finally:
                print("Turning off fan.")
                pwm.duty_cycle = 0
                pwm.deinit()
                request.set_value(GPIO_PIN_FAN, gpiod.line.Value.INACTIVE)

    def send_data_loop(self) -> None:
        while not self.__terminate.is_set():
            try:
                try:
                    temperature = self.__dht22.temperature
                    if temperature is not None:
                        self.__mqttClient.publish("sensor/dht22/inside/temperature", f"{temperature:.2f}", retain=True)
                except RuntimeError as error:
                    print(f"Failed reading temperature from DHT22 at GPIO 26: {error.args[0]}")
                try:
                    humidity = self.__dht22.humidity
                    if humidity is not None:
                        self.__mqttClient.publish("sensor/dht22/inside/humidity", f"{humidity:.2f}", retain=True)
                except RuntimeError as error:
                    print(f"Failed reading humidity from DHT22 at GPIO 26: {error.args[0]}")
            except Exception as error:
                self.__dht22.exit()
                raise error
            self.__terminate.wait(10.0)

    def main(self) -> None:
        self.test_lamp()
        self.test_fan()
        print("Reading sensors and sending to MQTT...")
        self.connect_mqtt()
        self.send_data_loop()


def main() -> None:
    main = Main()
    main.main()
