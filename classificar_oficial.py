from cgitb import text
import re
from xml.dom.minidom import Element
import pandas as pd
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from csv import reader
from bs4 import BeautifulSoup
import def_codigoPatente
from def_encontrarCNPJ import cnpj
#==============|| <funçoes utilizadas> ||===============#

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def encontrar_nome_patente(x):
    try:
        s = str(x).find('"')
        aux = str(x)[s:]
        e = aux[1:].find('"')
        if len(aux[:e+2])<5:
            return []
        return aux[:e+2]
    except:
        return[]

def retornar_patent(x):
    if len(def_codigoPatente.count_pc_by(x)) == 0:
        if len(encontrar_nome_patente(x)) != 0:
            return encontrar_nome_patente(x)
        else:
            return encontrar_proc(x)
    else:
        return def_codigoPatente.count_pc_by(x)

def encontrar_vigencia(x):
    try:
        if x.find('Inícioda vigência') >0:
            aux = x[x.find('Inícioda vigência'):]
            return aux[:aux.find('.')+1]
        if x.find('Início da vigência') >0:
            aux = x[x.find('Início da vigência'):]
            return aux[:aux.find('.')+1]
        if x.find('Vigência:') >0:
            aux = x[x.find('Vigência:'):]
            return aux[:aux.find('.')+1]
        if x.find('Início davigência') >0:
            aux = x[x.find('Início davigência'):]
            return aux[:aux.find('.')+1]

    except:
        return '[]'


def encontrar_dmy(x):
    try:    
        s = encontrar_vigencia(x).find('em')
        e = encontrar_vigencia(x).find('202')
        if encontrar_vigencia(x).find('202') == -1:
            e = encontrar_vigencia(x).find('201')
        if encontrar_vigencia(x).find('contar de') >0:
            s = encontrar_vigencia(x).find('contar de')
            return encontrar_vigencia(x)[s+10:e+4]
        if len(encontrar_vigencia(x)[s+3:e+4]) < 4:
            return '[]'
        return encontrar_vigencia(x)[s+3:e+4]
    except:
        return '[]'

def encontrar_proc(x):

    try:
        s = str(x).find('Proc.')
        e = s+27
        return x[s:e]
    except:
        return []

def final_p(x):
    if x[len(x)-1] == '.':
        return True
    else:
        return False
#==============|| <\funções utilizadas> ||===============#

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
                                            cont_final_p = 1
                                            aux_final_p = str(soup_documento.find_all(name='p')[j])[66:len(str(soup_documento.find_all(name='p')[j]))-4]
                                            while final_p(aux_final_p)==False:
                                                aux_final_p  += str(soup_documento.find_all(name='p')[j+cont_final_p])[66:len(str(soup_documento.find_all(name='p')[j+cont_final_p]))-4]
                                                cont_final_p+=1
                                            if len(def_codigoPatente.count_pc_by(aux_final_p)) == 0:
                                                if len(def_codigoPatente.count_pc_by(str(soup_documento.find_all(name='p')[j+1]))) > 0:
                                                    cont_final_p = 1
                                                    if final_p(aux_final_p+str(soup_documento.find_all(name='p')[j+1])[66:len(str(soup_documento.find_all(name='p')[j+1]))-4])==False:
                                                        while final_p(aux_final_p+str(soup_documento.find_all(name='p')[j+1])[66:len(str(soup_documento.find_all(name='p')[j+1]))-4])==False:
                                                            aux_final_p  += str(soup_documento.find_all(name='p')[j+cont_final_p])[66:len(str(soup_documento.find_all(name='p')[j+cont_final_p]))-4]
                                                            cont_final_p+=1
                                                    else:
                                                        lista_patente_link.append([links[0][l][0],remove_tags(aux_final_p+str(soup_documento.find_all(name='p')[j+1])[66:len(str(soup_documento.find_all(name='p')[j+1]))-4])])
                                                else:
                                                    lista_patente_link.append([links[0][l][0], remove_tags(aux_final_p)])
                                            else:
                                                lista_patente_link.append([links[0][l][0], remove_tags(aux_final_p)])
                                            
                                                   
                                            
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
lista_acordo_parceria = []
lista_termo_aditivo = []
lista_reconhecimento_titularidade = []

i = 0
while i<= len(lista_patente_link):
    try:

        #partilhamento
        if str(lista_patente_link[i][1]).find('Partilhamento') != -1:
            lista_patente_link[i].append('Contrato Partilhamento de Titularidade')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_partilhamento.append(lista_patente_link[i])
        #oferta tecnologica
        elif str(lista_patente_link[i][1]).find('Oferta Tecnológica') != -1:
            lista_patente_link[i].append('Oferta Tecnológica')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_oferta.append(lista_patente_link[i])
        #encomenda tecnologica
        elif str(lista_patente_link[i][1]).find('Encomenda Tecnológica') != -1:
            lista_patente_link[i].append('Contrato de Encomenda Tecnológica')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_encomenda.append(lista_patente_link[i])
        #distrato
        elif str(lista_patente_link[i][1]).find('Distrato ') != -1:
            lista_patente_link[i].append('Distrato ao Contrato de Licenciamento')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_distrato_licenciamento.append(lista_patente_link[i])
        #acordo de parceria
        elif str(lista_patente_link[i][1]).find('Acordo de Parceria') != -1:
            lista_patente_link[i].append('Acordo de Parceria')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_acordo_parceria.append(lista_patente_link[i])
        #termo-aditivo
        elif str(lista_patente_link[i][1]).find('Termo Aditivo') != -1:
            lista_patente_link[i].append('Termo Aditivo')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_termo_aditivo.append(lista_patente_link[i])
        #Reconhecimento de Titularidade
        elif str(lista_patente_link[i][1]).find('Reconhecimento de Titularidade') != -1:
            lista_patente_link[i].append('Reconhecimento de Titularidade')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
            lista_reconhecimento_titularidade.append(lista_patente_link[i])
        #licenciamento
        else:
            lista_patente_link[i].append('Licenciamento')
            lista_patente_link[i].append(retornar_patent(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_vigencia(lista_patente_link[i][1]))
            lista_patente_link[i].append(encontrar_dmy(lista_patente_link[i][1]))
            lista_patente_link[i].append(cnpj(lista_patente_link[i][1]))
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
  
todas_listas_classificados = [lista_partilhamento,
lista_oferta,lista_licenciamento,
lista_encomenda,lista_distrato_licenciamento, 
lista_acordo_parceria, lista_termo_aditivo, lista_reconhecimento_titularidade]

lista_classificado = []
i= 0
while i < len(todas_listas_classificados):
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

df = pd.DataFrame(lista_classificado, columns=['Link', 'Conteudo', 'Classificação', 'codigo', 'vigência', 'data_assinatura', 'cnpj'])

print(df)
df.to_csv("classificacao.csv", index = False)
