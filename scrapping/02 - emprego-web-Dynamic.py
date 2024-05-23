#https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#prerequisites
#problema para atualizar pip
#https://stackoverflow.com/questions/32639074/why-am-i-getting-importerror-no-module-named-pip-right-after-installing-pip
    #python -m ensurepip
    #python -m pip install --upgrade pip 



import requests 

def modoEstatico ():
    url = 'https://angular.io/' 
    response = requests.get(url) 
    html = response.text 
    print(html)

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

def modoDinamico (): 
    # url = 'https://angular.io/' 
    url = 'https://www.imovelweb.com.br/terrenos-venda-curitiba-pr.html?iv_=__iv_p_1_a_18378158614_g__w__h_1001634_ii__d_c_v__n_x_c__k__m__l__t__e__r__vi__&gclid=CjwKCAiAv9ucBhBXEiwA6N8nYDTgfMqlAbZI9uT1UBQOrnXVFiV2l7Uj9kCxhMFnGw93RiVW5DAwIRoCQLkQAvD_BwE' 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install())) 
    driver.get(url) 
    print(driver.page_source)

modoDinamico()