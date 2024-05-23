#https://blog.geekhunter.com.br/como-fazer-um-web-scraping-python/
#https://diegomariano.com/web-scraping-com-python/
from bs4 import BeautifulSoup
import requests

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta os dados do site
html = requests.get(site).content

# Formatando os dados
dados = BeautifulSoup(html, 'html.parser')
# print(dados.prettify())

# Coletando a div que armazena o email
email = dados.find("div", class_="email")
print(email)
print ("\n")
print(email.prettify())

# coletando a class email
email = dados.find("div", class_="email")

# coletando a tag dentro da div email
link = email.find("a")
print("1", link)  

# coletando apenas o texto
print("2", link.text)

# coletando o endereço do link
print("3", link.attrs['href'])