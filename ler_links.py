from cgitb import text
from xml.dom.minidom import Element
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
links = ['https://www.jusbrasil.com.br/diarios/1179164806/dou-secao-3-28-04-2022-pg-103', 'https://www.jusbrasil.com.br/diarios/1172398577/dou-secao-3-16-03-2022-pg-65', 'https://www.jusbrasil.com.br/diarios/1172886575/dou-secao-3-18-03-2022-pg-108', 'https://www.jusbrasil.com.br/diarios/1160175572/dou-secao-3-08-12-2021-pg-86', 'https://www.jusbrasil.com.br/diarios/1157537596/dou-secao-3-23-11-2021-pg-88']
patentes = []
print("segundos:",len(links)*7, "\nminutos:" ,(len(links)*7)/60, "\nhoras: ", ((len(links)*7)/60)/60)
l=0
while l< len(links):
    print("segundos:",(len(links)-l)*7, "\nminutos:" ,((len(links)-l)*7)/60, "\nhoras: ", (((len(links)-l)*7)/60)/60)
    try:
        #==============|| inicalizando a busca a partir dos links gerados ||===============#
        option = Options()
        option.headless = True
        driver = webdriver.Chrome()
        driver.get(links[l])

        #==============|| buscando os dados e encerrando a consulta ||===============#
        documento = driver.find_element_by_class_name('DocumentView-content-text')
        html_documento = html = documento.get_attribute('outerHTML')
        soup_documento = BeautifulSoup(html_documento, 'html.parser')
        driver.quit()

        #==============|| banco de palavras que validam em sua maior parte uma patente (UFMG) ||===============#
        lista_palavras_UFMG = ['Tecnologia','Licenciamento','exclusividade','LICENCIANTES',
        'LICENCIADA','Espécie', 'Tecnológica', 'Inovação', 'Objeto', 'INPI']
        #==============|| banco de palavras que validam em sua maior parte uma patente (UFMG) ||===============#
        lista_palavras_USP = ['Exclusiva', 'USP', 'Licença', 'Modalidade', 
        'Tecnologia', 'Parecer Jurídico', 'Exploração', 'Objeto', 'Vigência']

        #==============|| localizando a tag p que contem as possiveis patentes e adicionando em uma lista ||===============#

        def find_patente():
            maybe_patente = []
            j=0
            while j <= len(soup_documento.find_all(name='p')):
                i=0
                while True:
                    try:
                        if(str(soup_documento.find_all(name='p')[j]).find(lista_palavras_UFMG[i]) > 0):
                            maybe_patente.append(j)
                            if(maybe_patente.count(j)>=4):
                                if soup_documento.find_all(name='p')[j] in patentes:
                                    break  
                                else:
                                    if str(soup_documento.find_all(name='p')[j]).find('Programas de Computador') ==-1:
                                        patentes.append(soup_documento.find_all(name='p')[j])                
                    except:
                        break
                    i+=1
                j+=1
        find_patente()
    except:
        break
    l+=1
j=0

#==============|| estrutura de repetição para exibir todas as possiveis patentes em uma lista ||===============#
while True:
    try:
        print("\n\n",j,str(patentes[j])[66:])
    except:
        print("F")
        break
    j+=1