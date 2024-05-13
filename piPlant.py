# py für den RPi, zum analsysieren der Sensor-Daten und übermitteln an den Server

import RPi.GPIO as GPIO
# import board
import spidev
import time
import json
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def read_moisture():
    # Bodenfeuchtesensor auslesen
    result = GPIO.input(4)
    if result == 0:
        print("Boden ist Feucht")
    elif result == 1:
        print("Boden ist Trocken")
    return result

def read_channel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data

print("Start")

try:
    while True:
        # Bodenfeuchte und Feuchtigkeitssensor auslesen
        moisture = read_moisture()
        moisture_level = read_channel(0)
        print("Bodenfeuchte:", moisture)
        print("Feuchtigkeit:", moisture_level)

        # Daten in JSON-Format speichern
        sensor_data = {
            "bodenfeuchte": moisture,
            "feuchtigkeit": moisture_level,
        }

        print(sensor_data)

        # An den Server senden
        url = "http://193.196.54.229:8000/piPlant/SensorDatenEmpfang"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=sensor_data)
        response.raise_for_status()  # Ausnahme auslösen, wenn die Anfrage fehlschlägt
        print("Serverantwort:", response.text)
        time.sleep(660)  # 11 Minuten warten
except Exception as e:
    print("Fehler beim Senden der Daten an den Server:", e)

except KeyboardInterrupt:
    print("Abbruch.")

finally:
    GPIO.cleanup()
    spi.close()

print("Done")
