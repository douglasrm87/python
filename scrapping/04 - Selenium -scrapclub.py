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
import time 
 
options = webdriver.ChromeOptions() 
options.headless = True 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load target website 
url = 'https://scrapingclub.com/exercise/list_infinite_scroll/' 
 
# get website content 
driver.get(url) 

# instantiate items 
items = [] 
 
# instantiate height of webpage 
last_height = driver.execute_script('return document.body.scrollHeight') 
 
# set target count 
itemTargetCount = 20 
 
# scroll to bottom of webpage 
while itemTargetCount > len(items): 
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 
 
	# wait for content to load 
	time.sleep(1) 
 
	new_height = driver.execute_script('return document.body.scrollHeight') 
 
	if new_height == last_height: 
		break 
 
	last_height == new_height 
 
	# select elements by XPath 
	elements = driver.find_elements(By.XPATH, "//div[@class='card-body']/h4/a") 
	h4_texts = [element.text for element in elements] 
 
	items.extend(h4_texts) 
 
	# print title 
	print(h4_texts)