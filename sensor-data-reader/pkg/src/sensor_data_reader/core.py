import threading
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import gpiod
import os

MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = int(os.environ.get("MQTT_PORT"))
GPIO_CHIP_PATH = "/dev/gpiochip0"
GPIO_PIN_LIGHT = int(os.environ.get("GPIO_PIN_LIGHT"))
GPIO_PIN_FAN = int(os.environ.get("GPIO_PIN_FAN"))

class Main:
    def __init__(self):
        self.__terminate = threading.Event()
        self.__dht22 = adafruit_dht.DHT22(board.D26)
        self.__mqttClient = mqtt.Client(
            protocol=mqtt.MQTTv5
        )

    def connect_mqtt(self):
        try:
            self.__mqttClient.connect(MQTT_HOST, MQTT_PORT, 60)
        except Exception as e:
            raise e

    def test_lamp(self):
        with gpiod.request_lines(
            GPIO_CHIP_PATH,
            consumer="relay-test",
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

    def test_fan(self):
        with gpiod.request_lines(
            GPIO_CHIP_PATH,
            consumer="relay-test",
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
            self.__terminate.wait(10.0)
            print("Turning off fan.")
            request.set_value(GPIO_PIN_FAN, gpiod.line.Value.INACTIVE)

    def main(self):
        self.test_lamp()
        self.test_fan()
        print("Reading sensors and sending to MQTT...")
        self.connect_mqtt()
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


def main():
    main = Main()
    main.main()