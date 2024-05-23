import csv
import codecs
def lerCSV():
    comentAPP=csv.reader (codecs.open('psiclogia.csv', 'rU', 'utf-16'))
    for item in comentAPP:
        print (item)
        
lerCSV()