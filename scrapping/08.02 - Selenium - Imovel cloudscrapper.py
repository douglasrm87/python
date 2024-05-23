#Instalar
 
	#pip install cloudscraper
 

 
import pandas as pd
import cloudscraper as cl
from bs4 import BeautifulSoup
 
def mostrarTag (result,texto):
	cont = 0
	for tag in result:
		print(cont,texto,tag)	
		cont = cont + 1

def urlGenerica ():
	url = 'https://www.imovelweb.com.br/imobiliarias/jba-imoveis_15760037-terrenos-loteamento-condominio-venda-curitiba-pr.html?utm_source=google&utm_medium=cpc&ocultarDatos=true&iv_=__iv_p_1_a_1654900239_g_136261397649_w_dsa-1688507589007_h_1001634_ii_1001634_d_c_v__n_g_c_582965694368_k__m__l__t__e__r__vi__&gclid=CjwKCAiAheacBhB8EiwAItVO23nR0oeLqYGXStJmQVSttZ_ftBaFpKVvTcp4jF4fPjTrLKdtmpbsGhoCL2oQAvD_BwE'
	
	scraper = cl.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
	req = scraper.get(url)

	soup = BeautifulSoup(req.content, "html.parser")

	result = soup.find_all(attrs={"class" : "sc-ge2uzh-0"})
	# mostrarTag (result,"Atributo sc-ge2uzh-0")

	result = soup.find_all(attrs={"data-qa" : "expensas"})
	# mostrarTag (result,"Atributo data-qa")
	
		
	itens = soup.findAll(True, {'class':['sc-12dh9kl-4', 'sc-12dh9kl-2', 'sc-ge2uzh-0', 'sc-ge2uzh-2', 'sc-i1odl-10', 'sc-1uhtbxc-0']})
	mostrarTag (itens,"Atributos mesclados")
	



urlGenerica ( )

