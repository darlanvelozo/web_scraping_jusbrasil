from cgitb import text
from xml.dom.minidom import Element
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
links =['https://www.jusbrasil.com.br/diarios/77833080/dou-secao-3-07-10-2014-pg-61', 'https://www.jusbrasil.com.br/diarios/1172398577/dou-secao-3-16-03-2022-pg-65', 'https://www.jusbrasil.com.br/diarios/1160175572/dou-secao-3-08-12-2021-pg-86']


print("segundos:",len(links)*7, "\nminutos:" ,(len(links)*7)/60, "\nhoras: ", ((len(links)*7)/60)/60)
l=0

lista_links_Conteudo = []
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

        #==============|| localizando a tag p que contem as possiveis patentes e adicionando em uma lista ||===============#
        lista_links_Conteudo.append([links[l], soup_documento])
        
    except:
        break
    l+=1

j=0

while True:
    try:
        print(lista_links_Conteudo[j])
    except:
        print("F")
        break
    j+=1