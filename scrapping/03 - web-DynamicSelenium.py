#https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#prerequisites
#https://www.imovelweb.com.br/terrenos-venda-curitiba-pr.html?iv_=__iv_p_1_a_18378158614_g__w__h_1001634_ii__d_c_v__n_x_c__k__m__l__t__e__r__vi__&gclid=CjwKCAiAv9ucBhBXEiwA6N8nYDTgfMqlAbZI9uT1UBQOrnXVFiV2l7Uj9kCxhMFnGw93RiVW5DAwIRoCQLkQAvD_BwE
#problema para atualizar pip
#https://stackoverflow.com/questions/32639074/why-am-i-getting-importerror-no-module-named-pip-right-after-installing-pip
    #python -m ensurepip
    #python -m pip install --upgrade pip 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
# instantiate options 
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless = True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load website 
url = 'https://angular.io/' 
 
# get the entire website content 
driver.get(url) 
 
# select elements by class name 
elements = driver.find_elements(By.CLASS_NAME, 'text-container') 

for title in elements: 
	# select H2s, within element, by tag name 
	heading = title.find_element(By.TAG_NAME, 'h2').text 
	# print H2s 
	print(heading)