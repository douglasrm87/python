'
try:
    valorDesconto = int (input ("Digite o valor do desconto: "))
    orcamento = 10 * (1/valorDesconto)
    print ("Total: ",orcamento)
except ZeroDivisionError:
    print ("O valor digitado para o orçamento foi 0.")'