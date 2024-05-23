#Instalar
	#pip install selenium
	#pip install webdriver-manager
 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd

def listaItem (elements):
	cont = 0
	for element in elements:
		h4_texts = element.text
		print (cont," - Item Pesquisado: ",h4_texts)
		cont = cont + 1

options = webdriver.ChromeOptions() 
options.headless = True 
options.add_argument('--log-level=1')

driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 


def urlGenerica (url,tagHTML):
	# get website content 
	driver.get(url) 
	pesquisaGeral = driver.find_elements(By.XPATH, tagHTML) 
	listaItem (pesquisaGeral)
	matriz = [[],[]]
	for itemPandas in pesquisaGeral:
		matriz.append (itemPandas.text.strip().split("\n"))
	return matriz


url = 'https://www.apolar.com.br/venda/sao-jose-dos-pinhais/guatupe' 
tagHTML = "//*[@class='vue-property-item-apolar-search-engine']"
 
matriz = urlGenerica (url,tagHTML)

dataFramePandas = pd.DataFrame(matriz)
print (dataFramePandas)
dataFramePandas.to_csv("apolar.csv")