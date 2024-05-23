#04lercsv​
import csv
import codecs
comentariosAPP = {}
def lerCSV(coluna):
    cont = 0
    comentAPP=csv.reader (codecs.open('psiclogia.csv', 'rU', 'utf-16'))
    for item in comentAPP:
        if item[coluna]:
            comentariosAPP [cont] = item[coluna]
            cont = cont + 1
            # escolher a coluna que preciso.​
lerCSV(2)
print (comentariosAPP)