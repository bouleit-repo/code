# https://de.wikipedia.org/wiki/Schweizer_System#Anwendung_beim_Pétanque
import csv

thefile = open('/home/fb/bouleit/bouleit.github.io/README.md', 'w', 1)

thefile.write('# BOULE iT Turnier v0.1' + '\n')
thefile.write('Turnierteilnehmer die in einen Verein registriert sind, sollten durch ihre Zustimmung zur Vereins Datenschutz-Erklärung (DSVGO) zum speichern ihres Namens für die Dauer des Turniers und dessen Weitergabe an den Österreichischen Pétanque Verband bereits zugestimmt haben.' + '\n')
thefile.write('Im Falle eines Open-Turniers unterschreiben vereinslose Spieler die Datenschutz-Erklärung (DSVGO) bei der Registrierung / vor dem Beginn des Turniers.' + '\n')
thefile.write('### Schweizer System mit Buchholz-Wertung' + '\n')
thefile.write('### Teilnehmerliste:' + '\n')

# render table from .csv
with open('teilnehmer.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    thefile.write('\n')
    thefile.write('|' + 'NR' + '|' + 'NAME' + '|' + 'VEREIN' + '|' + 'SPIELER' + '|' +'\n')
    for row in reader:
        thefile.write('|' + row['NR'] + '|' + row['NAME'] + '|' + row['VEREIN'] + '|' + row['SPIELER'] + '|' +'\n')
    thefile.write('\n')

# are there any spare players?
thefile.write('### Freilos:' + '\n')

# render table from .csv
with open('freilos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    thefile.write('\n')
    thefile.write('|' + 'NR' + '|' + 'NAME' + '|' + 'VEREIN' + '|' + 'SPIELER' + '|' +'\n')
    for row in reader:
        thefile.write('|' + row['NR'] + '|' + row['NAME'] + '|' + row['VEREIN'] + '|' + row['SPIELER'] + '|' +'\n')
    thefile.write('\n')

# calculate round 1
thefile.write('### Runde 1:' + '\n')

# render table from .csv
with open('runde1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    thefile.write('\n')
    thefile.write('|' + 'NR' + '|' + 'NAME' + '|' + 'BAHN' + '|' + 'ERGEBNIS' + '|' +'\n')
    for row in reader:
        thefile.write('|' + row['NR'] + '|' + row['NAME'] + '|' + row['BAHN'] + '|' + row['ERGEBNIS'] + '|' +'\n')
    thefile.write('\n')


thefile.close()
