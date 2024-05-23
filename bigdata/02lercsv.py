import csv
import codecs
def lerCSV(coluna):
    comentAPP=csv.reader (codecs.open('psiclogia.csv', 'rU', 'utf-16'))
    for item in comentAPP:
        print (item[coluna])
lerCSV(2)