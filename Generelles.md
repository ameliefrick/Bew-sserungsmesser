### Protokoll 08.04.2024:

- Scrum-Master: Amelie
- Product Owner: Luis
- Head of Develop: Lukas


### Wünsche an das Team: 
- Kommunikation wichtig!!!! auch Besprechungen in Präsenz
- Weekly Termin auch als Arbeitstermin nutzen 



### Protokoll 10.04.2024:
- Festlegung des Produktziels:
  Bewässerungsmesser: Wasserstandsmesser, RPi, Website auf Server mit Statistischer Auswertung
  (+ digital LCD-Anzeige direkt am RPi für den aktuellsten Stand)

- Unterlagen:
  Risikoanalyse, Projektbericht (mit Abstrakt/Impact)

- Screenshort von Trello jeweils am Sprint Milestone Meeting zum Vergleich
- persönliche Berichte, Besprechnungsprotokolle und Trello anlegen und beim 2. Sprint zeigen

bis Dienstag: Recherche, Teile raussuchen konkret, Unterlagen (Risiko Luis, PA Amelie)


### Protokoll 18.04.2024:
- Recherchenergebnisse geteilt
- Sensorenteile "Feuchtigkeitssensor" Produkte herausgesucht
- Klärung der Projekteimzelnheiten mit Herr Paulin am nächsten Termin
- Fragen: Sensorwerte automatisch übernehmen/übergeben?
        Schlossensor einbinden, oder Codeausgabe?
        Zusatzanforderung Sinnvoll/realitätsnah? - Autom. Bewässerungspumpe statt Nachbar
        Richtiger Sensor?
        (Weitere Fragen bis Montag im Teamschat)

- Projektanforderungen erweitert:
  Wunsch von Herr Paulin, dass bei niedirgen Wasserstand Altert Nachbar
  benachrichtigt wird und Code für Zugang erhält für einen bestimmten Zeitraum.

- Projektinfos: Nicht nur Feuchtigkeit Unterwert sondern auch Höchstwert
  Primärserver von Lukas, alle setzen auber die selbe App auf. Geschriebener Code wird ausgetauscht untereinander.
  Vorteil für Bericht.
  

  To-Do:
  Termin mit Paulin für Montag ausmachen - Amelie

### Protokoll 22.04.24: ###
        Fragen: 
        Sensorwerte automatisch übernehmen/übergeben?
        - ??
        Schlossensor einbinden, oder Codeausgabe?
        - Nachbar hat Unfall, Code besser. Kontrolle wäre mit Cam prüfbar
        Zusatzanforderung Sinnvoll/realitätsnah? - Autom. Bewässerungspumpe statt Nachbar
        - Türchen/Pumpe/Klappe/Elektromagnet geht. Aufwand unklar
        Richtiger Sensor?
        -Recherche und selbst bestellen. Am besten den aus einer Anleitung an die man sich hält.

To-Do für folgendes Meeting:
  Klärung des Prozesses/Aufbau unseres Produkts jeder nochmal für sich selbst überlegen.
  Produkt sollte am Mittwoch grob stehen.

### Protokoll 25.04.2024:
- Bestellung des Feuchtigkeits-Sensors vorgenommen, sowie Keypad zur Code eingabe
- Product:
    Sensor mit Transformator hängt am RPi, dieser hat eine Verbindung zum Server welchem er die erhobenen Daten zur Analyse teilt.
    Auf diesem werden Statistiken graphisch dargestellt. Ist die Feuchtigkeit zu niedrig in den Pflanzen kann ein Dritte mit Zugangschip/     Zugangscode in die Wohnung mit dem jeweiligen Zugansmodul. Möglicher Weise wird die Website Accounts enthalten bei welchem der User       die Emails Dritter anlegen kann, welche den Code erhalten können.
    
To-Dos nächste Woche:
- Recherche Anleitungen für Plan des Gesamtprodukts
- Recherche Srum-Rollen und Aufgaben


### Protokoll 02.05.2024:
- Bericht erster Sprint Paulin:
  Progess-bericht (Amelie), Projekt-Dokumentation(Luis, Lukas)
  Bis Montag 06.05. jeder seinen Teil ins Word-Doc einpflegen,
  dann treffen über Teams um 12 Uhr.

  Bestellte Teile sind da. Liegen nicht vor, erst am 07.05.

  To-Dos: 
  - wie bisher
  - Fragen Paulin: Bewertung Code?, Sys3?, Noten?(Bericht, zwischenbericht, Präsentation)
  - Nächste Woche erste Aufgaben festlegen
  - Handson Termin für 07.02. im Anschluss Vorlesung
  - Mittwoch Termin bleibt für nächste Woche wie gehabt
 

### Protokoll 06.05.2024:
- gemeinsame Bearbeitung des Zwischenberichts
- Absenden des Berichts übernimmt Frau Frick heute um 19 Uhr
- HandsOn-Termin wird aufgrund der Vorlesungsplanumstellung, anschließendes TUtorium, zum Mittwochs-Termin dazugelegt
- Durch die Umstellung am Dienstag 07.05. werden an diesem Tag bereits die Sensoren übergeben von Frau Frick
- Es wurde ein Projekt/Produkt-Titel festgelegt: PiPlant Monitoring

### Protokoll 08.05.24:
- Frau Frick ist in den Pfingsferien unpässlich
- Mockup/Website bis Dienstag zum vorzeigen
- Server App aufsetzen und REST-API Thema klären bis vor den Ferien
- heute Test der Hardware und gekauften Sensor
    - es wurde festgestellt, dass ein weiteres Modul fehlt. Der Mcp3008. Wurde direkt bestellt 3x
- Aufgaben und Arbeitspakete überlegen für Zuweisung bis Montag Mittag: Termin nach Vorlesung online

### Protokoll 13.05.24:
- Hr Paulin hat Aufgaben im Projekt zugeteilt und diese sollten an diesem Tag bearbeitet werden
- Fr Frick sollte den request Entpunkt erstellen, sie hat bereits eine funktionierende App
- Hr Niederberger sollte den Emailversandt erstellen
- Ich sollte die python Datei erstellen auf dem Raspberry Pi, welche die Daten des Sensors ausliest und diese an den Server übergibt

- Am Abend gab es jeweils noch einige Fehlermeldungen

### Protokoll 14.05.24:
- Hr Niederberger konnte mit den MA des KIT das Problem lösen. Er verwendet seine HS-Mail mit dem MS 365 exchange Server
- Das hochladen der Daten funktioniert nun. Die Daten können in einer json Datei auf dem Server gespeichert werden
- Die Daten sind in einem Formsformat, dieses sollte als json umgewandelt werden zum upload und auf dem server ebenfalls

- weitere Aufgaben für diese Woche werden morgen vergeben

### Protokoll 15.05.24:
- Aufgaben-Verteilung für Arbeit bis zum Ende der Ferien.
- Sensoren werden morgen an die anderen Mitglieder von Herrn Kriegler vergeben
- Samstag 25.05. Meeting vereinbart für Zwischenstandsmeldung und Fragen

### Protokoll 06.06.2024:
- Trigger-Funktion für Email Versand vom Server an Email Nutzer(Nachbarn)           Lukas
- Festlegung des Schwellenwerts (Feuchtigkeit reicht nicht mehr aus) Dynamisch?     Luis/Amelie
- Funktion speichern der Codes und Url Endpunkt für Codeabfrage des Rpi             Lukas     
- gespeicherte Sensordaten übernehmen/auslesen für die Diagramme                    Lukas
- Diagramme in Website einbauen                                                     Amelie
Aufgaben bis Dienstag 11.06.2024

Weitere Funktionen und abschließender Zusammenbau alle Bestandteile/Funktionen nach er Budapest ausfahrt.

am 02.06. und 03.06. wurden weitere Arbeiten an den Funktionen vorgenommen.
Das Projekt wurde wider erwarten nicht getauscht. 


### Protokoll 20.06.2024:

Aufgaben unerledigt:
- Trigger-Funktion für Email Versand vom Server an Email Nutzer(Nachbarn)           Lukas
- Festlegung des Schwellenwerts (Feuchtigkeit reicht nicht mehr aus) Dynamisch?     Luis/Amelie
- Funktion speichern der Codes und Url Endpunkt für Codeabfrage des Rpi             Lukas
- Mobile-Ansicht Website Inhalt                                                     Lukas/Amelie
- aktuellen Code hochladen                                                          Lukas

Aufgaben anstehend:
- Termin für Probe-Präsentation/Aufbau nächste Woche finden                         Amelie
- Video vom Aufbau einstellen                                                       Luis
- Aufbau Modell Möglochkeiten erkunden                                              Luis
- Plakat gestalten                                                                  Amelie/Luis
- Plakat ausdrucken                                                                 Lukas

## bis nächsten Freitag 28.06.!!

Präsentation:
- A1 Plakat gestalten: Übersicht mit QE-Code zur Website
  (+ Infoflyer A5/6, kleine Version Plakat)
- (Werbesticker?)
- Pflanze mit Blumentopf    (Amelie)
- Raspberry-Aufbau und Zusatzkabel mitbringen
- Türe Simulation: Relais-Lämpchen (+ Motor?)
- Laptop für Grafik/Website
- Laptop/Handy für E-Mail-Empfang
- Raspberry 4/5 von Hochschule anstatt 400 (oder Lukas seinen falls nicht auch 400er)

  Aufbau:
- Raspberry in halben Schuhkarton mit Breadboard
- Sensor und Pflanze daneben
- Pinpad auf Karton/Plastikbox
- alles auf Brett (Holz/PVC) verkleben

### Protokoll 30.06.2024:
- Besprechung Projektfortschritt
- Amelie hat Plakat und Flyer gestaltet -> Absprache und letzte Änderungen
- neue Funktionen von Lukas auf bwCloud Server

## Todos bis morgen:
- Amelie: Plakat an Copy Shop schicken
- Amelie: Flyer an Lukas schicken
- Lukas und Luis: Code abgleichen für Verifizierung Zugangscode

## Mitbringen für Generalprobe:
- Amelie Pflanze
- Lukas Bildschirm und Laptop
- Luis Surface, Platte, RPi


  

  
