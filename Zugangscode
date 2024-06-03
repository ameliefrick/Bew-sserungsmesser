import json
import requests
import time
import hashlib
from datetime import datetime
import RPi.GPIO as GPIO

# Diese sind die GPIO-Pin-Nummern, an die die Zeilen der Keypad-Matrix angeschlossen sind
L1 = 5
L2 = 6
L3 = 13
L4 = 19

# Diese sind die vier Spalten
C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Die GPIO-Pin-Nummer der Spalte des Schlüssels, die derzeit gedrückt wird, oder -1, wenn kein Schlüssel gedrückt wird
keypad_gedrückt = -1

eingabe = ""

# Funktion zur Bereinigung der GPIO-Pins
def gpio_cleanup():
    GPIO.cleanup()

# GPIO-Setup
def gpio_setup():
    GPIO.setwarnings(False)
    GPIO.cleanup()  # Vor der Initialisierung bereinigen
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.OUT)  # Rotes Lämpchen
    GPIO.setup(23, GPIO.OUT)  # Theoretischer Zugang (z.B. Relais)

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

# Setzt alle Zeilen auf einen bestimmten Zustand. Dies ist eine Hilfe, um zu erkennen, wann der Benutzer eine Taste loslässt
def setze_alle_zeilen(status):
    GPIO.output(L1, status)
    GPIO.output(L2, status)
    GPIO.output(L3, status)
    GPIO.output(L4, status)

# Diese Callback-Funktion registriert die gedrückte Taste, wenn keine andere Taste derzeit gedrückt wird
def keypad_callback(channel):
    global keypad_gedrückt
    if keypad_gedrückt == -1:
        keypad_gedrückt = channel

# Liest die Spalten und fügt den entsprechenden Wert der Taste einer Variable hinzu
def lese_zeile(line, zeichen):
    global eingabe
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        eingabe = eingabe + zeichen[0]
    if(GPIO.input(C2) == 1):
        eingabe = eingabe + zeichen[1]
    if(GPIO.input(C3) == 1):
        eingabe = eingabe + zeichen[2]
    if(GPIO.input(C4) == 1):
        eingabe = eingabe + zeichen[3]
    GPIO.output(line, GPIO.LOW)

# Prüft spezielle Tasten
def prüfe_spezialtasten():
    global eingabe
    gedrückt = False
    GPIO.output(L3, GPIO.HIGH)

    if (GPIO.input(C4) == 1):
        print("Eingabe zurückgesetzt!")
        gedrückt = True

    GPIO.output(L3, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)

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

# Hauptprogramm
def hauptprogramm():
    global zugangscodes
    zugangscodes = zugangscodes_abrufen()
    try:
        while True:
            if keypad_gedrückt != -1:
                setze_alle_zeilen(GPIO.HIGH)
                if GPIO.input(keypad_gedrückt) == 0:
                    keypad_gedrückt = -1
                else:
                    time.sleep(0.1)
            else:
                if not prüfe_spezialtasten():
                    lese_zeile(L1, ["1","2","3","A"])
                    lese_zeile(L2, ["4","5","6","B"])
                    lese_zeile(L3, ["7","8","9","C"])
                    lese_zeile(L4, ["*","0","#","D"])
                    time.sleep(0.1)
                else:
                    time.sleep(0.1)
            if time.time() % 300 < 0.1:  # Alle 5 Minuten Zugangscodes aktualisieren
                zugangscodes = zugangscodes_abrufen()
    except KeyboardInterrupt:
        print("\nProgramm beendet.")
    finally:
        gpio_cleanup()

if __name__ == "__main__":
    gpio_setup()
    try:
        GPIO.add_event_detect(C1, GPIO.RISING, callback=keypad_callback)
        GPIO.add_event_detect(C2, GPIO.RISING, callback=keypad_callback)
        GPIO.add_event_detect(C3, GPIO.RISING, callback=keypad_callback)
        GPIO.add_event_detect(C4, GPIO.RISING, callback=keypad_callback)
        hauptprogramm()
    except RuntimeError as e:
        print("Fehler beim Hinzufügen der Flankenerkennung:", e)
        gpio_cleanup()
        exit(1)


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
