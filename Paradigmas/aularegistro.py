import requests 
query = {"cep":82640570,"formato":"json"} 
response = requests.get('http://cep.republicavirtual.com.br/web_cep.php',params=query)
print ("Retorno Http:",response)
print ("Conteúdo Http:",response.json())
# Usando  Iteração
#
for coluna, conteudo in response.json().items():
	print(coluna, conteudo)
