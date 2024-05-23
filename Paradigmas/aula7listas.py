vetorX = []
TAM = 5
cont = 0
soma = 0
mult = 1
while (cont < TAM):
    num = int (input ("Digite um numero:"))
    vetorX.append(num)
    cont = cont + 1
cont = 0

while (cont < TAM):
    soma = soma + vetorX[cont]
    mult = mult * vetorX[cont]
    cont  = cont + 1

print ("Soma Total:" , soma)
print ("Multiplicação Total:",mult)
cont = 0
while (cont < TAM):
    print ("Valor lido: " , vetorX[cont])
    cont = cont + 1
