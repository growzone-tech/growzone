import threading
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import os

MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = os.environ.get("MQTT_PORT")

class Main:
    def __init__(self):
        self.__terminate = threading.Event()
        self.__dht22 = adafruit_dht.DHT22(board.D26)
        self.__mqttClient = mqtt.Client()

    def connect_mqtt(self):
        try:
            self.__mqttClient.connect(MQTT_HOST, MQTT_PORT, 60)
        except Exception as e:
            raise e

    def main(self):
        self.connect_mqtt()
        while not self.__terminate.is_set():
            try:
                temperature = self.__dht22.temperature
                humidity = self.__dht22.humidity
                if temperature is not None:
                    self.__mqttClient.publish("sensor/dht22/inside/temperature", f"{temperature:.2f}", retain=True)
                if humidity is not None:
                    self.__mqttClient.publish("sensor/dht22/inside/humidity", f"{humidity:.2f}", retain=True)
            except RuntimeError as error:
                # This library throws a RuntimeError for almost every missed pulse.
                # We just print and keep going.
                print(f"Failed reading DHT22 at PIN 26: {error.args[0]}")
                time.sleep(2.0)
                continue
            except Exception as error:
                dht_device.exit()
                raise error
            self.__terminate.wait(10.0)


def main():
    main = Main()
    main.main()