import threading
# import board
# import adafruit_dht
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os

MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = int(os.environ.get("MQTT_PORT"))
GPIO_PIN_LIGHT = int(os.environ.get("GPIO_PIN_LIGHT"))
GPIO_PIN_FAN = int(os.environ.get("GPIO_PIN_FAN"))

class Main:
    def __init__(self):
        self.__terminate = threading.Event()
        # self.__dht22 = adafruit_dht.DHT22(board.D26)
        self.__mqttClient = mqtt.Client()

    def connect_mqtt(self):
        try:
            self.__mqttClient.connect(MQTT_HOST, MQTT_PORT, 60)
        except Exception as e:
            raise e

    def test_lamp(self):
        print("Turning on light.")
        GPIO.output(GPIO_PIN_LIGHT, GPIO.HIGH)
        self.__terminate.wait(10.0)
        print("Turning off light.")
        GPIO.output(GPIO_PIN_LIGHT, GPIO.LOW)

    def test_fan(self):
        print("Turning on fan.")
        GPIO.output(GPIO_PIN_FAN, GPIO.HIGH)
        self.__terminate.wait(10.0)
        print("Turning off fan.")
        GPIO.output(GPIO_PIN_FAN, GPIO.LOW)

    def main(self):
        self.test_lamp()
        self.test_fan()
        self.connect_mqtt()
        while not self.__terminate.is_set():
            try:
                pass
                # temperature = self.__dht22.temperature
                # humidity = self.__dht22.humidity
                # if temperature is not None:
                #     self.__mqttClient.publish("sensor/dht22/inside/temperature", f"{temperature:.2f}", retain=True)
                # if humidity is not None:
                #     self.__mqttClient.publish("sensor/dht22/inside/humidity", f"{humidity:.2f}", retain=True)
            except RuntimeError as error:
                # This library throws a RuntimeError for almost every missed pulse.
                # We just print and keep going.
                # print(f"Failed reading DHT22 at PIN 26: {error.args[0]}")
                self.__terminate.wait(2.0)
                continue
            except Exception as error:
                # self.__dht22.exit()
                raise error
            self.__terminate.wait(10.0)


def main():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIO_PIN_LIGHT, GPIO.OUT)
        GPIO.setup(GPIO_PIN_FAN, GPIO.OUT)
        main = Main()
        main.main()
    finally:
        GPIO.cleanup()