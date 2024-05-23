 
def gibonacci(n):                            #linha1
    if n<=1:                                 #linha2
        return n                             #linha3
    else:      
        return gibonacci(n-1) - gibonacci(n-2)

# n = int(input('Exibir ate o termo (maior que 2): '))
for val in range(0,12):
    print(gibonacci(val))

# a = -1 
# b = -1
# c = a - (-b)
# print ("Valor de :",c)
# ret = gibonacci(7)     
# # 0 1 1 2 3 5 8
# print ("Valor final: ",ret)