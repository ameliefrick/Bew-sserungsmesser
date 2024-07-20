# Keypad



import RPi.GPIO as GPIO

import time

import requests



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



# URL des Servers und Endpunkt fÃ¼r Zugangscodes

def get_url():

    global input_code

    return f"http://193.196.54.157:8000/se4/validation?code={input_code}"



# Zugangscodes an Server schicken

def zugangscodes_pruefen():

    global return_final

    try:

        response = requests.get(get_url())

        if response.status_code == 200:

            des_response = response.json()

            return_final = des_response.get("result")

        else:

            print("Fehler beim Abrufen der Zugangscodes:", response.status_code)

            #return None

        if return_final == True:

            return True

        else: 

            return False

            print("Code falsch")

        

        

    except requests.exceptions.RequestException as e:

        print("Ein Fehler ist aufgetreten:", e)

        return None

        



# Korrekter Code



input_code = ""



# GPIO-Pins fÃ¼r Relais und rote LED

RELAY_PIN = 4

RED_LED_PIN = 17



GPIO.setup(RELAY_PIN, GPIO.OUT, initial = GPIO.HIGH)

#GPIO.setup(RELAY_PIN, GPIO.PUD_UP)

GPIO.setup(RED_LED_PIN, GPIO.OUT)



# StandardzustÃ¤nde

#GPIO.output(RELAY_PIN, GPIO.HIGH)

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

                

                if zugangscodes_pruefen() == True:

                    print("Code korrekt! Relais wird geschaltet.")

                    GPIO.output(RELAY_PIN, GPIO.LOW)

                    time.sleep(5)

                    GPIO.output(RELAY_PIN, GPIO.HIGH)

                    print("Code wieder eingeben")

                else:

                    print("Falscher Code! Rote LED wird fuer 5 Sekunden aktiviert.")

                    GPIO.output(RED_LED_PIN, GPIO.HIGH)

                    time.sleep(5)  # Rote LED fÃ¼r 5 Sekunden aktivieren

                    GPIO.output(RED_LED_PIN, GPIO.LOW)  # Rote LED ausschalten

                input_code = ""

            elif key == '*': 

                print("Eingabe zurueckgesetzt.")

                print("Code erneut eingeben")

            else:

                if len(input_code) < 6:

                    input_code += str(key)

                    print(f"Taste gedrueckt: {key}")

        time.sleep(0.5)  # Kurze Pause zwischen den SchleifendurchlÃ¤ufen, um die CPU nicht zu belasten



except KeyboardInterrupt:

    pass

finally:

    GPIO.cleanup()

    print("Abgeschlossen")

