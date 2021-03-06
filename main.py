# https://de.wikipedia.org/wiki/Schweizer_System#Anwendung_beim_Pétanque
import csv

thefile = open('/home/fb/bouleit/bouleit.github.io/README.md', 'w', 1)

thefile.write('# BOULE iT Turnier 01.01.2020' + '\n')
# write 'Last refresh hh.mm.ss'
thefile.write('Durch die Verwendung der „BOULE iT Turnier“ Internetseite stimmen Sie für die Dauer des Turniers zu, dass Ihre Angaben (Name, Lizenznummer, Name des Vereins) laut EU-Datenschutz-Grundverordnung (DSGVO) gespeichert und genutzt werden, beziehungsweise dass die Ergebnisse nach dem Turnier an den Österreichischen Pétanque Verband weitergegeben werden.' + '\n')
# thefile.write('Bei Open-Turniers unterschreiben Spieler die in ihren Verein die Datenschutz-Erklärung (laut DSVGO) noch nicht unterschrieben haben, sowie vereinslose Spieler die Datenschutz-Erklärung (laut DSVGO) bei der Registrierung / vor dem Beginn des Turniers.' + '\n')
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
