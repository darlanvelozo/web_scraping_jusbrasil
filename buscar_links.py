from cgitb import text
from xml.dom.minidom import Element
from requests import options
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
from csv import reader
from bs4 import BeautifulSoup

#==============|| gerando a busca ||===============#
url = 'https://www.jusbrasil.com.br'
pesquisa = '/diarios/busca?q='
busca = str(input('siga o padrão abaixo \nexemplo do padrão de busca -> "UFMG"+"licenciamento"\nexemplo do padrão de busca -> "usp"+"patente"+"licença"\n\ndigite os valores de busca conforme o exemplo: '))

buscaFinal = url+pesquisa+busca
#==============|| acessando o site ||===============#
option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(buscaFinal)

#==============|| capturando os elementos da pagina ||===============#
element = driver.find_element_by_class_name('SearchResults-documents')
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser')
driver.quit()
links = []
for link in soup.findAll('a'):
    if len(link.get('href')) >=35 and link.get('href')[42] != '?' :
        links.append(link.get('href'))

#==============|| exibindo links das paginas do diario ||===============#
i=0
while True:
    try:
        print(links[i])
    except:
        break
    i+=1

#==============|| estrutura de repetição para capturar a quantidade de dados desejados ||===============#
input_controle = str(input('vai querer mais uma pag [s/n]'))
i=2
while input_controle != 'n':
    
    url1 = 'https://www.jusbrasil.com.br/diarios/busca?q='+busca+'&p='+str(i)
    option = Options()
    option.headless = True
    driver = webdriver.Chrome()
    driver.get(url1)

    #==============|| capturando os elementos da pagina ||===============#
    element = driver.find_element_by_class_name('SearchResults-documents')
    html = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    for link in soup.findAll('a'):
        if len(link.get('href')) >=35 and link.get('href')[42] != '?' :
            links.append(link.get('href'))
    i+=1
    print(len(links))

    input_controle = str(input('vai querer mais uma pag [s/n]'))
i=0

#==============|| exibindo todos os links das paginas dos diarios ||===============#
while True:
    try:
        print(links[i])
    except:
        break
    i+=1    
print("\n\n",links)

df = pd.DataFrame(links)
df.to_csv("links.csv", index = False)

