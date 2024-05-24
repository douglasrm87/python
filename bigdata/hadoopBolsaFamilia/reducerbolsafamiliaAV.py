#Fonte da planilha: https://www.portaltransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos
# python .\mapperbolsafamiliaAV.py | sort | python .\reducerbolsafamiliaAV.py
# cd C:/Desenvolvimemto/Fontes/python/bigdata/hadoopBolsaFamilia
import sys
acumulador = 0.0
estadoAnt = "AC"
dictBolsa = {estadoAnt: 0.0}
dadosBolsa = [ "AC:10.90"
              ,"AM:40.90"
              ,"PR:100.00"
              ,"PR:50.80" ]
for line in sys.stdin:
#for line in dadosBolsa:
    line = line.split (":")
    estado = line[0].strip()
    valor = line[1].strip()
    if (estadoAnt == estado):
        acumulador = acumulador + float(valor)
        dictBolsa.update({estadoAnt:acumulador})
    else:
        #print ("Troca estado: %s\t%s" % (estadoAnt,acumulador))
        acumulador = float(valor)
        dictBolsa.update({estado:acumulador})
        estadoAnt = estado
def formatar_valor_br(my_value):
    a = '{:,.2f}'.format(float(my_value))
    return a
for k, v in dictBolsa.items():
    print ("%s\t%s" % (k, formatar_valor_br(v)))
