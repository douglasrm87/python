print ("ola python")
#Entrada
av1 = 0
av2 = 0
indicadorAV3 = 0
 
av1 = int (input ("Digite Nota 01:"))
if (av1 < 40):
    indicadorAV3 = 1
print ("Eu li Av1:", av1)
av2 = int (input ("Digite Nota 02:"))
if (av1 < 40 and av2 < 40):
    print ("reprovado")
else:
    if (av2 < 40 ):
        indicadorAV3 = 1

print ("Eu li Av2:", av2)
#processamento
media = (av1 + av2) /2
print ("media:", media)
if (media >= 60 and indicadorAV3 == 0):
    print ("aprovado")
else:
    if (indicadorAV3 == 1):
         av3 = int (input ("Digite Nota 03:"))
         if (av1 < av2 ):
             media = (av3 + av2)/2
         else:
            media = (av3 + av1)/2
         if (media < 60):
            print ("reprovado")
         else:
            print ("Aprovado")