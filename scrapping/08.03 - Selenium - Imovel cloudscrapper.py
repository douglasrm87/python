#Instalar
 	#pip install cloudscraper

	#Uso do metodo string para pegar somente texto
		# https://pytutorial.com/find-all-by-class-with-python-beautifulsoup
	#Uso do metodo get_text para pegar somente texto
		#https://stackoverflow.com/questions/34660417/beautiful-soup-if-class-contains-or-regex
 

 
import pandas as pd
import cloudscraper as cl
from bs4 import BeautifulSoup
 
def mostrarTag (result,texto):
	cont = 0
	for tag in result:
		print(cont,texto,tag.get_text()) 
		cont = cont + 1

def urlGenerica ():
	url = 'https://www.imovelweb.com.br/imobiliarias/jba-imoveis_15760037-terrenos-loteamento-condominio-venda-curitiba-pr.html?utm_source=google&utm_medium=cpc&ocultarDatos=true&iv_=__iv_p_1_a_1654900239_g_136261397649_w_dsa-1688507589007_h_1001634_ii_1001634_d_c_v__n_g_c_582965694368_k__m__l__t__e__r__vi__&gclid=CjwKCAiAheacBhB8EiwAItVO23nR0oeLqYGXStJmQVSttZ_ftBaFpKVvTcp4jF4fPjTrLKdtmpbsGhoCL2oQAvD_BwE'
	
	scraper = cl.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
	req = scraper.get(url)

	soup = BeautifulSoup(req.content, "html.parser")

	itens = soup.findAll(True, {'class':['sc-12dh9kl-4', 'sc-12dh9kl-2', 'sc-ge2uzh-0', 'sc-ge2uzh-2', 'sc-i1odl-10', 'sc-1uhtbxc-0']})
	
	# print (itens.text)
	mostrarTag (itens,"Atributos mesclados")
	
	dataFramePandas = pd.DataFrame(itens)
	print (dataFramePandas)
	dataFramePandas.to_csv("imovelweb.csv")


urlGenerica ( )

