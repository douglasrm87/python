#https://silviolima07.medium.com/web-scrap-7e99db63e8e0
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def scrap_imovel_web(n):
  print("Pagina:",n)
 
  url_page = 'https://www.imovelweb.com.br/apartamentos-venda-sao-paulo-sp-mais-de-1-banheiro-mais-de-1-vaga-de-10-a-20-anos-pagina'

  print(url_page+'-'+str(n)+'.html')
  scrap = requests.get(url_page+'-'+str(n)+'.html')
  soup = BeautifulSoup(scrap.content, 'html.parser')
#   print (soup)

  # Classes localizadas através do inspect feito na página
  class_main_features = soup.find_all(class_ = "main-features")
  class_posting_location = soup.find_all('span',class_ = "posting-location go-to-posting")
  class_first_price = soup.find_all(class_ = "first-price")

  tag_features = class_main_features
  tag_location = class_posting_location
  tag_price = class_first_price


  pattern_qto = '[1-90-9 ]*Q[a-z]*' # Quarto ok
  pattern_vaga = '[0-9 ]*V[a-z]+' # Vagas ok
  pattern_area = '[0-9][0-9]*[ ]m²[ áa-zú]*' # area util ok        
  pattern_banheiro = '[0-90-9]* B[a-z]+' # Banheiro ok
  pattern_endereco = '<span>[ :alnum:]+[ [íÍáiÓêA-Za-zaúçíéôáãa-zoiÍ]*' # endereço ok# Aplicação das expressões regulares para trazer as linhas com informações em cada página pesquisada

  # Cada página tinha 20 linhas de cada informação, esse valor deve ser igual pra todos items.
  quarto = re.findall(pattern_qto, str(tag_features))
  vaga = re.findall(pattern_vaga, str(tag_features))
  banheiro = re.findall(pattern_banheiro, str(tag_features))
  area = re.findall(pattern_area, str(tag_features))
  endereco = re.findall(pattern_endereco, str(tag_location))

  ##################################################################
  
  # A informação price, precisou de duas etapas, por isso possui dois padrões para aplicação das expressões regulares
  pattern_temp = 'data-price=["R[$ 0-9.]*'  # mostrar price ok
  pattern = 'R[$ 0-9.]*'

  temp = re.findall(pattern_temp, str(tag_price)) 
  price = re.findall(pattern, str(temp))
  
  print (temp)

  ##################################################################

  # Pode-se aplicar a função e trazer todas informações de uma vez ou separadamente, comentando a linha do return e deixando
  # apenas a variável desejada. Foi feito dessa forma, para garantir que todas viessem em número de 20 por página.
  # Nas tentativas de trazer todas juntas de uma vez, em alguns momentos, vinha 19 para algumas e isso não permitia a criação do
  # dataset final com todas informações agrupadas por página pesquisada
  print("Concluido")
  # banheiro, quarto, vaga , endereco, price , area
  # out1       out2   out3   out4      out5    out6
  return  vaga #, banheiro ,quarto, vaga , endereco, price , area


# Foram criadas listas vazias que irão armazenar as informações obtidas em cada página
#
quarto =[] # lista com valores de quartos
vaga =[] # lista com os valores de vaga
banheiro =[] # lista com os valores de banheiro
area_total =[] # lista com valores da area total
area_util=[] # lista com valores de area util
endereco=[] # lista de bairros
price=[]

# banheiro, quarto, vaga , endereco, price , area
# out1       out2   out3   out4      out5    out6
for page in range(1,20):
    out1 = scrap_imovel_web(page) # A função ira receber o numero da pagina e trazer informações de banheiro, conforme esta definido na função
    # print("Banheiro:", len(out1)," Quarto:", len(out2), " Vaga:", len(out3), " endereco:", len(out4), "price:", len(out5),"area:", len(out6))
    print("Banheiro:", len(out1))

# for page in range(1,201): # Ir da pagina 1 a 500
    #out1, out2, out3, out4, out5, out6 = scrap_imovel_web(page) 
    # out1 = scrap_imovel_web(page) # A função ira receber o numero da pagina e trazer informações de banheiro, conforme esta definido na função
    # print("Banheiro:", len(out1)," Quarto:", len(out2), " Vaga:", len(out3), " endereco:", len(out4), "price:", len(out5),"area:", len(out6))
    # print("Banheiro:", len(out1))
    
    # Nesse caso ja sabemos que cada página deve ter 20 itens
    # for i in range(20):                   # out1, out2 e out3 se deu tudo certo, tem o mesmo tamanho, esse valor sera o range de iteração
    #     banheiro.append(out1[i])                 # a lista hrefs recebera os href contido na posicao de indice 'i' na lista out1
        # quarto.append(out2[i])                   # o mesmo para a lista prices que recebera o price em out2
        # vaga.append(out3[i])
        # endereco.append(out4[i])
        # price.append(out5[i])
                            
    # for n in range(0,len(out6),2):               # out6 tem 40 linhas, sendo pares igual area total e impares area util
    #     area_total.append(out6[n][0:16])         # 0, 2, 4, 6, 8, 10,...
    #     area_util.append(out6[n+1][0:16])        # 1, 3, 5, 7, 9, 11


data = { 'area_total': area_total,
         'area_util': area_util,
         'quarto': quarto,
          'banheiro': banheiro,
          'vaga': vaga,
          'bairro': endereco,
         'price': price}    
      
df_vendas = pd.DataFrame(data, columns=['price', 'area_total', 'area_util', 'quarto', 'banheiro', 'vaga', 'bairro'])
print (df_vendas)
df_vendas.to_csv("imovelweb_venda.csv")
# ret = scrap_imovel_web(1)
# print (ret)