cpf = "028450949"

def validarCPF (cpf, intervalo):
    contador  =  len (cpf) - 1
    somaDigito = 0
    for c in range(2,intervalo):
        print (cpf[contador]," * ",c)
        somaDigito = somaDigito + ((int (cpf[contador]) * c))
        contador -= 1
    print ("Soma: ", somaDigito)
    dig = 11 - (somaDigito%11)
    if (dig >=10):
        return 0
    return dig
   

dig01 = validarCPF (cpf, 11)
print ("Digito 01: ", dig01)
cpf = cpf + str (dig01)
print ("Novo CPF:",cpf)

dig02 = validarCPF (cpf, 12)
print ("Digito 01: ", dig02)
cpf = cpf + str (dig02)
print ("Novo CPF:",cpf)