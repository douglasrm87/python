
cad = input ("Digite sua palavra:")
print ("Palavra digitada:", cad)
print ("Primeira letra palavra digitada:", cad [0])

cap_p = True
while cap_p and (len(cad) >= 2):
    cap_p = cap_p and (cad[0] == cad[-1])
    #remove as letras da extremidade
    cad = cad[1:-1]

print ("A palavra ",cad[0:5:2])  

print ("cap_p:",cap_p) 
if (cap_p == True):
    print ("A palavra ",cad," é Palindromo/capicua.")  
else:
    print ("A palavra digitada: ",cad," não é Palindromo/capicua.")   