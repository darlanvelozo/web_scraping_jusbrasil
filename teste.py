from ast import Return
from distutils.log import error
import re
import def_codigoPatente
def count_pc_by(text):
    try:  
        list_rgx1 = [
                     '[A-Z][A-Z]\d{7}-\d',
                     '[A-Z][A-Z]\d{11}[A-Z]\d',
                     '[A-Z][A-z]\d\d\d\d\d[A-z]\d\d\d',
                     '[A-Z][A-Z]\d\d[A-z]\d\d\d\d\d\d\d',
                     '[A-Z][A-Z]\d{8}-[A-Z]\d',
                     '[A-Z][A-Z]\d{8}[A-Z]\d',
                     '[A-Z][A-z]\d{11}',
                     '[A-Z][A-z]\d{10}',
                     '[A-Z][A-z]\d{9}',
                     '[A-Z][A-Z]\d{7}',
                     '[A-Z][A-z]\d{5,7}',
                     '[A-Z]\.[A-Z]\.\sPat\.\sNo.\s\d\,\d\d\d\,\d\d\d',
                     '[A-Z][A-Z].{1,20}\d\,\d\d\d\,\d\d\d',
                     '[A-Z]\.[A-Z].{1,20}\d\,\d\d\d\,\d\d\d',
                     '\d\,\d\d\d\,\d\d\d'
                    ]
        list_rgx2 = ['[A-Z][A-Z] \d{6,12}',
                     "[A-Z][A-Z] \d{1}\W\d{3}\W\d{3}",
                     '[A-Z][A-Z]\d{6,12}',
                     '[A-Z][A-Z][A-Z][A-Z]\d{6,12}',
                     '[A-Z][A-Z] \d{2,4}.\d{6,12}',
                     '[A-Z][A-Z] \d{6,12}.\d{1,2}',
                     '[A-Z][A-Z] \d\d \d{4} \d{6} \d',
                     '[A-Z][A-Z] \d\d \d{4} \d{7}',
                     '[A-Z][A-Z] \d{12}-\d',
                     '[A-Z][A-Z] \d{2} \d{4} \d{6}-\d',
                     '\d\d/\d{6}',
                     '[A-Z][A-Z] \d{6} \d{6} \d',
                     '[A-Z][A-Z]\d\d \d{4} \d{6} \d',
                     
                     ]

        pcs = []

        for rgx in (list_rgx1):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED1+ ")
              pcs.append(r)

         # procurando regex - LISTA 2
        for rgx in (list_rgx2):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED2+ ")
              pcs.append(r)
        
    
        # print("PATENT CITATION's Puras ==============")
        # print("Total -> ", len(pcs))
        # for p in pcs:
        #   print(" ===> ", p)
        # print("PATENT CITATION's Puras==============")

        return pcs
    except Exception as e:
        return 'No answer' + str(e)



x = ' Espécie: Proc. 23072.046821/2018-81- EDITAL Nº 01, DE 07 DE DEZEMBRO DE 2021. A Universidade Federal de Minas Gerais - UFMG - CNPJ nº 17.217.985/0001-04, por meio de sua Coordenadoria de Transferência e Inovação Tecnológica - CTIT, e a Fundação de Amparo à Pesquisa do Estado de Minas Gerais - FAPEMIG - CNPJ nº 21.949.888/0001-83, em atendimento ao Disposto no Art. <a class="cite" href="https://www.jusbrasil.com.br/topicos/10936577/artigo-6-da-lei-n-10973-de-02-de-dezembro-de-2004" rel="10936577" title="Artigo 6 da Lei nº 10.973 de 02 de Dezembro de 2004">6º</a> da Lei <a class="cite" href="https://www.jusbrasil.com.br/legislacao/1033799/lei-da-inovacao-lei-10973-04" rel="10937399,15679993" title="Lei no 10.973, de 2 de dezembro de 2004.">10.973</a>/04 - <a class="cite" href="https://www.jusbrasil.com.br/legislacao/1033799/lei-da-inovacao-lei-10973-04" rel="10937399" title="Lei no 10.973, de 2 de dezembro de 2004.">Lei de Inovacao</a>, tornam público o presente Edital de Oferta Tecnológica Pública para o Licenciamento, com exclusividade, no Brasil, dos direitos para uso, desenvolvimento, industrialização e comercialização da tecnologia consubstanciada no know how intitulado: Uso de linhagem não-toxigênica de bactéria para prevenção da infecção e/ou colonização por Clostridium difficile, registrado pela Coordenadoria de Transferência e Inovação Tecnológica em 06/08/2021 sob o número 202100007, mediante condições estipuladas no Edital e seus anexos. OBJETO DO CONTRATO: Licenciamento da tecnologia supra mencionada, de titularidade da UFMG e da FAPEMIG. ENTREGA DAS PROPOSTAS até 14 de janeiro de 2022 às 17h00min. Endereço: Coordenadoria de Transferência e Inovação Tecnológica - CTIT, na Avenida Antônio Carlos, nº 6.627, Unidade Administrativa II, 2º andar, sala 2011, Bairro Pampulha, Belo Horizonte, Minas Gerais, Brasil, CEP: 31.270-901. O Edital e seus Anexos poderão ser acessados na íntegra pela página eletrônica da UFMG/CTIT - www.ctit.ufmg.br. Mais esclarecimentos por escrito via e-mail info@ctit.ufmg.br.'
'''y = 'da vigência: o presente instrumento terá vigência de 10 (dez) anos, a contar da data'
z = 'de sua assinatura, em 10 de março de 2022 . Nomes e cargos dos signatários: o Prof. Gilberto Medeiros Ribeiro - Diretor da CTIT/UFMG, o Sr. Marcos Heleno Guerson de Oliveira Junior - Presidente do INMETRO, os Srs. Cassiano Rabelo e Silva e Hudson Luiz Silva de Miranda - Diretores da FABNS, o Prof. Jaime Arturo Ramírez - Presidente da FUNDEP.'
lista = []
lista.append(x)
lista.append(y)
lista.append(z)
'''
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

'''def remove_tags(text):
    ''.join(xml.etree.ElementTree.fromstring(text).itertext())

'''

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)



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
def encontrar_nome_patente(x):
    try:
        s = str(x).find('"')
        aux = str(x)[s:]
        e = aux[1:].find('"')
        if len(aux[:e+2])<5:
            return []
        return aux[:e+2]
    except:
        return []

'''
def final_p(x):
    if x[len(x)-1] == '.':
        return True
    else:
        return False
'''
'''aux_final_p = x[0]
cont_final_p = 1
while True:
    if final_p(aux_final_p) == False:
        aux_final_p  += x[cont_final_p]
        cont_final_p+=1
    else:
        print(aux_final_p)
        break'''
#print(encontrar_nome_patente(x))

def retornar_patent(x):
    if len(count_pc_by(x)) == 0:
        if len(encontrar_nome_patente(x)) != 0:
            return encontrar_nome_patente(x)
        else:
            return encontrar_proc(x)
    else:
        return count_pc_by(x)
'''print(encontrar_vigencia(x))
print(encontrar_dmy(x))
print(encontrar_proc(x))'''

print(retornar_patent(x))

print(x)
print(remove_tags(x))