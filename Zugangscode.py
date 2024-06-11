#keypad-Funktion

#1. teil: Funktion und Eingabe

import RPi.GPIO as GPIO
import time

# GPIO-Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Keypad-Definition
KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

ROW_PINS = [5, 6, 13, 19]   # BCM Nummern der Row-Pins
COL_PINS = [12, 16, 20, 21] # BCM Nummern der Column-Pins

for pin in ROW_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for pin in COL_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Korrekter Code
CORRECT_CODE = "1234"
input_code = ""

# GPIO-Pins für Relais und rote LED
RELAY_PIN = 26
RED_LED_PIN = 4

GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# Standardzustände
GPIO.output(RELAY_PIN, GPIO.LOW)
GPIO.output(RED_LED_PIN, GPIO.LOW)

def read_keypad():
    for row in range(4):
        GPIO.output(COL_PINS[row], GPIO.HIGH)
        for col in range(4):
            if GPIO.input(ROW_PINS[col]) == GPIO.HIGH:
                GPIO.output(COL_PINS[row], GPIO.LOW)
                return KEYPAD[col][row]
        GPIO.output(COL_PINS[row], GPIO.LOW)
    return None

print("Start")

try:
    while True:
        key = read_keypad()
        if key is not None:
            if key == '#':
                if input_code == CORRECT_CODE:
                    print("Code korrekt! Relais wird geschaltet.")
                    GPIO.output(RELAY_PIN, GPIO.HIGH)
                else:
                    print("Falscher Code! Rote LED wird für 5 Sekunden aktiviert.")
                    GPIO.output(RED_LED_PIN, GPIO.HIGH)
                    time.sleep(5)  # Rote LED für 5 Sekunden aktivieren
                    GPIO.output(RED_LED_PIN, GPIO.LOW)  # Rote LED ausschalten
                input_code = ""
            elif key == '*':
                input_code = ""
                GPIO.output(RELAY_PIN, GPIO.LOW)
                print("Eingabe zurückgesetzt.")
            else:
                if len(input_code) < 4:
                    input_code += str(key)
                    print(f"Taste gedrückt: {key}")
        time.sleep(0.5)  # Kurze Pause zwischen den Schleifendurchläufen, um die CPU nicht zu belasten

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("Abgeschlossen")


# 2. Teil: Code Prüfung und Abfrage

# Funktion zur Bereinigung der GPIO-Pins
def gpio_cleanup():
    GPIO.cleanup()

# URL des Servers und Endpunkt für Zugangscodes
url = "http://193.196.54.229:8000/piPlant/Zugangscodes"

# Zugangscodes regelmäßig vom Server abrufen
def zugangscodes_abrufen():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Fehler beim Abrufen der Zugangscodes:", response.status_code)
        return []

#Abfrage ob code noch gültig!

    if (not gedrückt and GPIO.input(C4) == 1):
        hashed_eingabe = hashlib.sha256(eingabe.encode()).hexdigest()
        if hashed_eingabe in zugangscodes:
            print("Zugangscode korrekt!")
            GPIO.output(23, GPIO.HIGH)  # Zugang öffnen (z.B. Relais aktivieren)
            time.sleep(5)  # Zugang für 5 Sekunden öffnen
            GPIO.output(23, GPIO.LOW)
        else:
            print("Zugangscode falsch!")
            GPIO.output(18, GPIO.HIGH)  # Rotes Lämpchen einschalten
            time.sleep(5)  # Lämpchen für 5 Sekunden leuchten lassen
            GPIO.output(18, GPIO.LOW)
        gedrückt = True

    GPIO.output(L3, GPIO.LOW)

    if gedrückt:
        eingabe = ""

    return gedrückt


# Erläuterungen

# GPIO-Setup: Die GPIO-Pins für das Keypad und die LEDs werden initialisiert.

# Keypad-Callback: Eine Callback-Funktion, die den gedrückten Key registriert.

# Zugangscodes vom Server abrufen: Eine Funktion, die die Zugangscodes vom Server abruft und in einer Liste speichert.

# Eingabe lesen: Funktionen, die die Eingabe vom Keypad lesen und spezielle Tasten wie "A" und "C" behandeln.

# Zugangscode prüfen: Funktion, die den eingegebenen Zugangscode hasht und mit den abgerufenen Zugangscodes vergleicht.

# Hauptprogramm: Eine Endlosschleife, die die Eingabe vom Keypad liest, die Zugangscodes prüft und alle 5 Minuten aktualisiert.

# Hinweise
# Hashing: Der Zugangscode wird mit SHA-256 gehashed, bevor er mit den abgerufenen Zugangscodes verglichen wird.
# Keypad-Logik: Die Tasten "A" und "C" haben spezielle Funktionen (Überprüfung und Zurücksetzung der Eingabe).
# Zeitverzögerungen: Es gibt kleine Verzögerungen (time.sleep(0.1)), um Entprellen zu vermeiden und die Eingaben zu stabilisieren.
# GPIO-Cleanup: Die GPIO-Pins werden am Ende des Programms aufgeräumt.
