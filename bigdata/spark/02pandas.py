#https://www.geeksforgeeks.org/pandas-groupby/
import pandas as pd

data1 = {'Name':['Douglas', 'Pedro', 'Douglas', 'Jose',
                 'Gaurav', 'Pedro', 'Jose', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Rua Sao Jose', 'Rua Souza Naves', 'Kannuaj',
                   'Jaunpur', 'Rua Sao Jose', 'Rua Souza Naves', 'Aligarh'],
        'Qualification':['Mestre', 'Especialista', 'Tecnico', 'Phd',
                         'Formado', 'Segundo Grau', 'Mestre', 'Especialista']}
df = pd.DataFrame(data1)                   
print ("\nMostrando DataFrame montado")
print (df)

print ("\nAgrupando por nome")
df.groupby('Name')
grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()

print ("\nEscolhendo um grupo apenas")
print (grp.get_group('Douglas'))
print ("\nAgrupnado por Qualificação")
grp = df.groupby('Qualification')
for name, group in grp:
    print(name)
    print(group)
    print()

print ("Pandas")