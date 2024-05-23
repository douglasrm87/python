#https://jbaimoveis.com.br/venda/terreno/curitiba/
#https://www.scrapingbee.com/blog/selenium-python/
#problema para atualizar pip
#https://stackoverflow.com/questions/32639074/why-am-i-getting-importerror-no-module-named-pip-right-after-installing-pip
    #python -m ensurepip
    #python -m pip install --upgrade pip 

# Por Th e tr
	# 	https://iqss.github.io/dss-webscrape/finding-web-elements.html
	# //*[@id="table"]/tbody/tr[2]/th

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time 
 
options = webdriver.ChromeOptions() 
options.headless = True 
options.add_argument('--log-level=1')

driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 

# load target website 
url = 'https://jbaimoveis.com.br/venda/terreno/curitiba/' 
 
# get website content 
driver.get(url) 

# instantiate items 
items = [] 
 
# instantiate height of webpage 
last_height = driver.execute_script('return document.body.scrollHeight') 
 
# set target count 
itemTargetCount = 20 
 

all_links = driver.find_elements(By.TAG_NAME, 'p')
# elements = driver.find_elements(By.XPATH, "//h3") 
# elements = driver.find_elements(By.XPATH, "//p") 
# elements = driver.find_elements(By.TAG_NAME, "p") 

# //*[@id="table"]/tbody/tr[2]/th
elements = driver.find_elements(By.CLASS_NAME, "titulo-grid") 
h4_texts = [element.text for element in elements] 
print (h4_texts)

elements = driver.find_elements(By.XPATH, "//*[@itemprop='streetAddress']") 
cont = 0
for element in elements:
	h4_texts = element.text
	print (cont," - Endereço: ",h4_texts)
	cont = cont + 1
print ("\n\nElementos encontrados \n\n\n: ",h4_texts)
cont = 0

# elements = driver.find_elements(By.XPATH, "//*[@itemprop='streetAddress']") 
# for element in elements:
# 	h4_texts = element.text
# 	print (cont , " - Endereço: ",h4_texts)
# 	cont = cont + 1
# print ("\n\nElementos encontrados \n\n\n: ",h4_texts)
