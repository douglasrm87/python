#Instalar
 
	#pip install cloudscraper
 

 
import pandas as pd
import cloudscraper as cl
from bs4 import BeautifulSoup
 
def urlGenerica ():
	url = 'https://www.imovelweb.com.br/imobiliarias/jba-imoveis_15760037-terrenos-loteamento-condominio-venda-curitiba-pr.html?utm_source=google&utm_medium=cpc&ocultarDatos=true&iv_=__iv_p_1_a_1654900239_g_136261397649_w_dsa-1688507589007_h_1001634_ii_1001634_d_c_v__n_g_c_582965694368_k__m__l__t__e__r__vi__&gclid=CjwKCAiAheacBhB8EiwAItVO23nR0oeLqYGXStJmQVSttZ_ftBaFpKVvTcp4jF4fPjTrLKdtmpbsGhoCL2oQAvD_BwE'
	
	scraper = cl.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
	req = scraper.get(url)

	soup = BeautifulSoup(req.content, "html.parser")

	result = soup.find_all(attrs={"class" : "sc-ge2uzh-0"})
	# print("Enderecos: ",result)
	result = soup.find_all(attrs={"data-qa" : "expensas"})
	print ("Valor: ",result)	

	tags = {tag.name for tag in soup.find_all()}
	# iterate all tags
	for tag in result:
		# find all element of tag
		print("Atributo data-qa: ",tag)	
	

urlGenerica ( )

