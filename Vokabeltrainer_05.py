#!/usr/bin/env python
# coding: utf-8

# # Vokabeltrainer, geschrieben in Python 3.7, 3.8
# ## angefangen von Papa, weiterzuentwickeln von Paul 2023

# **Neue Funktion im Sept. 2023**
# Die Vokabel-Dateien werden alternativ direkt aus einem Google sheet geladen
# **Neue Funktion im Okt. 2023**
# Anpassungen für das Surface Tablet.

print("Vokabeltrainer wird geladen...")
print("______________________________")
print("")

import datetime
import openpyxl
import os
import pandas
import random
from IPython.display import HTML

allgemeiner_Pfad='.'
sheeturl=False # False lädt eine Datei von der lokalen Festplatte
Schluesselliste=[['Englisch','14ymLVXnWKFUXAAgZ2oPCVh3M44IuE-K1',''],
                 ['Latein','12dzw07OguBhtL_gqTHWlQ5sn5SS9LubN',''],
                ]
Schluessel_Dataframe=pandas.DataFrame(Schluesselliste, columns=['Sprache', 'Schluessel','Dateiame'])

alle_Dateien=os.walk(allgemeiner_Pfad)
for Verzeichnisname,Unterverzeichnisname,Dateiname in alle_Dateien:
    for d in Dateiname:
        if d.endswith('xlsx'):
            Schluessel_Dataframe.loc[len(Schluessel_Dataframe)]=['','',d]

print('Folgende Vokabeldateischlüssel stehen zur Verfügung:')
print(Schluessel_Dataframe)
print('Bitte wähle einen Schlüssel:')

Indexwahl=-1
while Indexwahl not in range(0,len(Schluessel_Dataframe['Sprache'])):
    Indexwahl=int(input())
gewaehlter_Schluessel=Schluessel_Dataframe.loc[Indexwahl]['Schluessel']
gewaehlter_Dateiname=Schluessel_Dataframe.loc[Indexwahl]['Dateiame']
print("Vokabeldatei wird geladen. Bitte warten.")
Vokabeldateischluessel=gewaehlter_Schluessel
Vokabeldateipfad=allgemeiner_Pfad+'/'+gewaehlter_Dateiname
if gewaehlter_Dateiname=='':
    sheeturl=True # True lädt eine Datei von Google Drive
elif gewaehlter_Schluessel=='':
    sheeturl=False # False lädt eine Datei von der lokalen Festplatte
else:
    print('Fehler bei der Auswahl der Vokabeldatei. Bitte Programm neu starten.')

def Zeitstempel():
    return str(datetime.datetime.now()).replace(' ','_').replace('.','-').replace(':','-')

googlesheeturl_start="https://docs.google.com/spreadsheets/d/"
googlesheeturl_ende="/export?format=xlsx"
googlesheeturl=googlesheeturl_start+Vokabeldateischluessel+googlesheeturl_ende

if sheeturl==True:
    Vokabeln=pandas.read_excel(googlesheeturl) # wird über das Internet von Google Drive geladen
else:
    Vokabeln=pandas.read_excel(Vokabeldateipfad) # wird von der lokalen Festplatte geladen

print("Die geladene Datei hat folgende Spalten:")
print(str(Vokabeln.columns))

Vokabeln=Vokabeln[Vokabeln["Deutsch"].notna()]
Anzahlvokabeln=len(Vokabeln)
print("Ich habe "+str(Anzahlvokabeln)+" Vokabeln geladen.")

Sprache1=str(Vokabeln.columns[0])
Sprache2=str(Vokabeln.columns[1])
print("Ich habe in Deiner Datei folgende Spalten mit Sprachen identifiziert:")
print(Sprache1+', '+Sprache2)

Reihenfolge=0
while Reihenfolge!="1" and Reihenfolge!="2":
    print("In welcher Reihenfolge soll ich abfragen?")
    print("1: "+Sprache1+" eingeben")
    print("2: "+Sprache2+" eingeben")
    Reihenfolge=input()

# ändere die Reihenfolge, um die Richtung der Abfrage zu ändern
if Reihenfolge=="2":
    Vok1=Vokabeln[Sprache1].tolist()
    Vok2=Vokabeln[Sprache2].tolist()
elif Reihenfolge=="1":
    Vok2=Vokabeln[Sprache1].tolist()
    Vok1=Vokabeln[Sprache2].tolist()
else:
    print("Feher. Programm bitte neu starten.")

#Zufallszahlen erzeugen
print("Wie viele Vokablen soll ich abfragen?")
Anzahlfragen=int(input())

#Fragen, ob nur die neueren Vokabeln unten in der Datei gefragt werden sollen:
print("Soll ich nur die [n]eueren Vokabeln oder aus [a]llen Vokabeln die Fragen auswählen? Gib n oder a ein.")
welcheVokabeln=input()
while welcheVokabeln!="a" and welcheVokabeln!="n":
  print("Gibt n oder a ein")
if welcheVokabeln=="a":
  Startzahl=0
else:
  Startzahl=int(Anzahlvokabeln-Anzahlfragen)
Fragenliste=random.sample(range(Startzahl, Anzahlvokabeln), Anzahlfragen)
print("Ich werde Dich jetzt folgende Vokabeln abfragen: "+str(Fragenliste))

Linie="_________________________________________"
gefragt=0
richtig=0
falsche_Antworten=[] # leere Liste
Fragennummer=1
for a in Fragenliste:
    print(str(Fragennummer)+") "+Vok1[a])
    Antwort=input()
    Fragennummer+=1
    if Antwort!="quit()":
        gefragt+=1
        if Antwort==Vok2[a]:
            print("Richtig!")
            print(Linie)
            richtig+=1
        else:
            print("Falsch! Die Antwort wäre gewesen: "+Vok2[a])
            falsche_Antworten.append(a)
            print("Denkst Du, dass Du dennoch richtig geantwortet hast? (j/n)")
            rifa=input()
            if rifa=="j":
                richtig+=1
            print(Linie)
    else:
        break
print("Du hast "+str(richtig)+" von "+str(gefragt)+" richtig beantwortet.")

# Rechen die Note, z.B print(6-18/20*5)
Note=6-richtig/gefragt*5
print("Deine Note ist "+str(Note)+".")

# falsche Vokabeln in Datei schreiben
Fehlerdateiname=Zeitstempel()+'_Fehlerdatei_'+Sprache1+'.xlsx'
Fehlerdateipfad=allgemeiner_Pfad+'/'+Fehlerdateiname
print(Fehlerdateipfad)

falsche_Vokabeln=Vokabeln.loc[falsche_Antworten] # suche die falsche beantworteten Vokabeln und schreibe sie in einen neuen Dataframe.
print('Du hast folgende Vokabeln falsch beantwortet:')
print(falsche_Vokabeln)

falsche_Vokabeln.to_excel(Fehlerdateipfad,index=False)
