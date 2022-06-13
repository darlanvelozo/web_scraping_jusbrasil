x = 'Espécie: Proc. 23072.257749/2021-11 - Contrato de Licenciamento para exploração das criações consubstanciadas de Tecnologia que entre si celebram a Universidade Federal de Minas Gerais - UFMG - CNPJ nº 17.217.985/0001-04, por meio de sua Coordenadoria de Transferência e Inovação Tecnológica - CTIT, o Instituto Nacional de Metrologia, Qualidade e Tecnologia - INMETRO - CNPJ nº 00.662.270/0003-20, conjuntamente denominadas LICENCIANTES, e a FABNS Fábrica de Nanosoluçõese Participações Ltda. - CNPJ nº 36.615.002/0001-32, doravante denominada LICENCIADA, com interveniência da Fundação de Desenvolvimento da Pesquisa - FUNDEP - CNPJ nº 18.720.938/0001-41. Objeto: Constitui objeto do presente Contrato de Licenciamento, a título oneroso, sem exclusividade, pelas Licenciantes à Licenciada, dos direitos para uso, desenvolvimento, produção, exploração comercial, prestação de serviços ou obtenção de qualquer vantagem econômica relacionada à Tecnologia intitulada "Dispositivo metálico para microscopia por varredura por sonda e método de fabricação do mesmo", depositada junto ao Instituto Nacional de Propriedade Industrial - INPI, sob o número BR 1020160291267, em 12/12/2016, e à Tecnologia intitulada "dispositivo metálico para microscopia e espectroscopia óptica de campo próximo e método de fabricação do mesmo", depositada junto ao Instituto Nacional de Propriedade Industrial - INPI, sob o número BR 1020150103522, em 07/05/2015. Início'
y = 'da vigência: o presente instrumento terá vigência de 10 (dez) anos, a contar da data'
z = 'de sua assinatura, em 10 de março de 2022 . Nomes e cargos dos signatários: o Prof. Gilberto Medeiros Ribeiro - Diretor da CTIT/UFMG, o Sr. Marcos Heleno Guerson de Oliveira Junior - Presidente do INMETRO, os Srs. Cassiano Rabelo e Silva e Hudson Luiz Silva de Miranda - Diretores da FABNS, o Prof. Jaime Arturo Ramírez - Presidente da FUNDEP.'
lista = []
lista.append(x)
lista.append(y)
lista.append(z)

def encontrar_vigencia(x):
    try:
        aux = x[x.find('Início da vigência'):]
        return aux[:aux.find('.')+1]
    except:
        return '[]'

print(encontrar_vigencia(x))

def encontrar_dmy(x):
    try:    
        s = encontrar_vigencia(x).find('em')
        e = encontrar_vigencia(x).find('202')
        return encontrar_vigencia(x)[s+3:e+4]
        
    except:
        return '[]'

def final_p(x):
    if x[len(x)-1] == '.':
        return True
    else:
        return False

aux_final_p = x[0]
cont_final_p = 1
while True:
    if final_p(aux_final_p) == False:
        aux_final_p  += x[cont_final_p]
        cont_final_p+=1
    else:
        print(aux_final_p)
        break