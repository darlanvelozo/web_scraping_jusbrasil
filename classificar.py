from cgitb import text
from xml.dom.minidom import Element
import pandas as pd
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from csv import reader
from bs4 import BeautifulSoup
import def_codigoPatente

links = []
with open('links.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    list_of_rows.remove(list('0'))

links.append(list_of_rows)


universidade = int(input("[0] -> UFMG\n[1] -> USP\n\nDigite sua opção: "))
lista_patente_link=[]
patentes = []
print("segundos:",len(links[0])*7, "\nminutos:" ,(len(links[0])*7)/60, "\nhoras: ", ((len(links[0])*7)/60)/60)
def ler_todos_links():
    l=0
    while l<= len(links[0]):
        print("segundos:",(len(links[0])-l)*7, "\nminutos:" ,((len(links[0])-l)*7)/60, "\nhoras: ", (((len(links[0])-l)*7)/60)/60)
        try:
            #==============|| inicalizando a busca a partir dos links gerados ||===============#
            option = Options()
            option.headless = True
            driver = webdriver.Chrome()
            driver.get(links[0][l][0])

            #==============|| buscando os dados e encerrando a consulta ||===============#
            documento = driver.find_element_by_class_name('DocumentView-content-text')
            html_documento = html = documento.get_attribute('outerHTML')
            soup_documento = BeautifulSoup(html_documento, 'html.parser')
            driver.quit()

            #==============|| banco_de_listas[0] = UFMG/ banco_de_listas[1] = USP ||===============#
            banco_de_listas=[
            #==============|| banco de palavras que validam em sua maior parte uma patente (UFMG) ||===============#
            ['Tecnologia','Licenciamento','exclusividade','LICENCIANTES','LICENCIADA','Espécie', 'Tecnológica', 'Inovação', 'Objeto', 'INPI'], 
            #==============|| banco de palavras que validam em sua maior parte uma patente (USP) ||===============#
            ['Exclusiva', 'USP', 'Licença', 'Modalidade', 'Tecnologia', 'Parecer Jurídico', 'Exploração', 'Objeto', 'Vigência', 'Licenciamento', 'patente']]


            #==============|| localizando a tag p que contem as possiveis patentes e adicionando em uma lista ||===============#

            def find_patente():
                maybe_patente = []
                j=0
                while j <= len(soup_documento.find_all(name='p')):
                    i=0
                    while True:
                        try:
                            if(str(soup_documento.find_all(name='p')[j]).find(banco_de_listas[universidade][i]) > 0):
                                maybe_patente.append(j)
                                if(maybe_patente.count(j)>=4):
                                    if soup_documento.find_all(name='p')[j] in patentes:
                                        break  
                                    else:
                                        if str(soup_documento.find_all(name='p')[j]).find('Programas de Computador') ==-1:
                                            patentes.append(soup_documento.find_all(name='p')[j])
                                            lista_patente_link.append([links[0][l][0],str(soup_documento.find_all(name='p')[j])[66:]])

                                                        
                        except:
                            break
                        i+=1
                    j+=1
            find_patente()
        except:
            break
        l+=1

ler_todos_links()


#==============|| adicionando os conteudos em suas listas para organizar a classificação ||===============#

lista_partilhamento = []
lista_oferta = []
lista_licenciamento = []
lista_encomenda = []
lista_distrato_licenciamento = []


i = 0
while i<= len(lista_patente_link):
    try:
        if str(lista_patente_link[i][1]).find('Partilhamento') != -1:
            lista_patente_link[i].append('Contrato Partilhamento de Titularidade')
            
            lista_patente_link[i].append(def_codigoPatente.count_pc_by(lista_patente_link[i][1]))
            lista_partilhamento.append(lista_patente_link[i])
        elif str(lista_patente_link[i][1]).find('Oferta Tecnológica') != -1:
            lista_patente_link[i].append('Oferta Tecnológica')
            
            lista_patente_link[i].append(def_codigoPatente.count_pc_by(lista_patente_link[i][1]))
            lista_oferta.append(lista_patente_link[i])
        elif str(lista_patente_link[i][1]).find('Encomenda Tecnológica') != -1:
            lista_patente_link[i].append('Contrato de Encomenda Tecnológica')
            
            lista_patente_link[i].append(def_codigoPatente.count_pc_by(lista_patente_link[i][1]))
            lista_encomenda.append(lista_patente_link[i])
        elif str(lista_patente_link[i][1]).find('Distrato ') != -1:
            lista_patente_link[i].append('Distrato ao Contrato de Licenciamento')
            lista_patente_link[i].append(def_codigoPatente.count_pc_by(lista_patente_link[i][1]))
            lista_distrato_licenciamento.append(lista_patente_link[i])
        else:
            lista_patente_link[i].append('Licenciamento')
            lista_patente_link[i].append(def_codigoPatente.count_pc_by(lista_patente_link[i][1]))
            lista_licenciamento.append(lista_patente_link[i])
            print(def_codigoPatente.count_pc_by(lista_patente_link[i][1]))
        
    except:
        break
    i+=1
    


i=0
#==============|| estrutura de repetição para exibir todas as possiveis patentes em uma lista ||===============#
j=0
while True:
    try:
        print("classificação: Contrato Partilhamento de Titularidade\n","link: ",lista_partilhamento[j][0],"\n",str(lista_partilhamento[j][1])[66:])
        print("classificação: Oferta Tecnológica\n","link: ",lista_oferta[j][0],"\n",str(lista_oferta[j][1])[66:])
        print("classificação: Licenciamento\n","link: ",lista_licenciamento[j][0],"\n",str(lista_licenciamento[j][1])[66:])
        print("classificação: Contrato de Encomenda Tecnológica\n","link: ",lista_encomenda[j][0],"\n",str(lista_encomenda[j][1])[66:])
        print("classificação: Distrato ao Contrato de Licenciamento\n","link: ",lista_distrato_licenciamento[j][0],"\n",str(lista_distrato_licenciamento[j][1])[66:])
        #print("\n\n",j,': ', lista_patente_link[j][0],"\n",str(lista_patente_link[j][1])[66:])
        #print("\n\n",j,str(patentes[j])[66:])
    except:
        print("F")
        break
    j+=1
  
todas_listas_classificados = [lista_partilhamento,lista_oferta,lista_licenciamento,lista_encomenda,lista_distrato_licenciamento]
lista_classificado = []
i= 0
while i < 5:
    k=0
    while k <= len(todas_listas_classificados[i]):
        try:
            if todas_listas_classificados[i][k] in lista_classificado:
                print()
            else:    
                lista_classificado.append(todas_listas_classificados[i][k])
        except:
            break
        k+=1
    i+=1

df = pd.DataFrame(lista_classificado, columns=['Link', 'Conteudo', 'Classificação', 'codigo'])

print(df)
df.to_csv("classificacao.csv", index = False)
