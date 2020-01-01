# https://de.wikipedia.org/wiki/Schweizer_System#Anwendung_beim_Pétanque
import csv

thefile = open('/home/fb/bouleit/bouleit.github.io/README.md', 'w', 1)

thefile.write('# Boule iT Turnier' + '\n')
thefile.write('## Schweizer System mit Buchholz-Wertung' + '\n')
thefile.write('## Teilnehmerliste:' + '\n')

with open('/home/fb/bouleit/bouleit.github.io/teilnehmer.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    thefile.write('|' + 'NR' + '|' + 'NAME' + '|' + 'VEREIN' + '|' + 'SPIELER' + '|' +'\n')
    for row in reader:
        thefile.write('|' + row['NR'] + '|' + row['NAME'] + '|' + row['VEREIN'] + '|' + row['SPIELER'] + '|' +'\n')

thefile.close()
