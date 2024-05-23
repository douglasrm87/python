porcentagem20 = 1.20
porcentagem15 = 1.15
porcentagem10 = 1.10
porcentagem5 = 1.05

def reajustar (salario,porcentagem):
    novoSalario = salario * porcentagem
    aumento = novoSalario - salario
    print("Seu salario é: R$", salario,"\nCom reajuste de: ",porcentagem ,"\nCom um aumento de: R$", aumento, "\nSendo assim seu novo salario é: R$ {:.2f}".format(novoSalario))

porcentagem = 0
salario = float(input("Insira o seu salario: "))
if (salario <= 280.00):
    porcentagem = porcentagem20
elif (salario <= 700.00):
    porcentagem =  porcentagem15
elif (salario <= 1500.00):
    porcentagem =  porcentagem10
else:
    porcentagem =  porcentagem5
reajustar (salario,porcentagem)