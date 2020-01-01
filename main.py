# https://de.wikipedia.org/wiki/Schweizer_System#Anwendung_beim_Pétanque
import csv

thefile = open('/home/fb/bouleit/bouleit.github.io/README.md', 'w', 1)

thefile.write('# Boule iT Turnier v0.1' + '\n')
thefile.write('## Schweizer System mit Buchholz-Wertung' + '\n')
thefile.write('## Teilnehmerliste:' + '\n')

# render table from .csv
with open('teilnehmer.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    thefile.write('\n')
    thefile.write('|' + 'NR' + '|' + 'NAME' + '|' + 'VEREIN' + '|' + 'SPIELER' + '|' +'\n')
    for row in reader:
        thefile.write('|' + row['NR'] + '|' + row['NAME'] + '|' + row['VEREIN'] + '|' + row['SPIELER'] + '|' +'\n')
    thefile.write('\n')

# are there any spare players?
thefile.write('## Freilos:' + '\n')

thefile.close()
