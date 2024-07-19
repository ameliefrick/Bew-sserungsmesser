# py für den RPi, zum analsysieren der Sensor-Daten und übermitteln an den Server

#PiPlant: Feuchtigkeitsmesser

import RPi.GPIO as GPIO
import spidev #für den Sensor
import time #für sleep-Funktion
import datetime #für Zeitstempel
import json
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

#Spi-Setup für Feuchtigkeitssensor
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def read_channel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data

print("Start")

try:
    while True:
        # Feuchtigkeitssensor auslesen
        moisture_level = read_channel(0)
        print("Feuchtigkeit:", moisture_level)

        # Daten in JSON-Format speichern als Formparameter für header
        sensor_data = {
            "feuchtigkeit": moisture_level,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        #zu json serialisieren:
        json_data = json.dumps(sensor_data)

        print(sensor_data)

        url = "http://193.196.54.229:8000/piPlant/SensorDatenEmpfang"
        url1 = "http://193.196.54.157:8000/se4/SensorDatenEmpfang"

        headers = {'Content-Type': 'application/json',}
        response = requests.post(url, data=json_data, headers=headers)
        response1 = requests.post(url1, data=json_data, headers=headers)
        
        print("Serverantwort:", response.content.decode())
        print("Serverantwort 2:", response1.content.decode())
        time.sleep(660)  # 11 Minuten warten wegen Sensor (müssen mind 10 sein) = 660

except Exception as e:
    print("Fehler beim Senden der Daten an den Server:", e)

except KeyboardInterrupt:
    print("Abbruch.")

finally:
    GPIO.cleanup()
    spi.close()

print("Done")
