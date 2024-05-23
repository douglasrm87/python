#Fazer uma função que recebe três argumentos, e que retorne o produto desses
#  três argumentos.

#resultado = 1,5,20,60,120
#fat - 5,4,3,2,1

def fatorial (fat):
    resultado = 1
    while fat > 1:
        resultado = fat * resultado
        fat = fat - 1
    return resultado

print (fatorial (5))
print (fatorial (6))
print (fatorial (9))




 
