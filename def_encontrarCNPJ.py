import re

def cnpj(text):
    try:  
        list_rgx1 = [
            '([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})',
            '([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})'
                    ]
        list_rgx2 = [
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
        '''for rgx in (list_rgx2):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED2+ ")
              pcs.append(r)
        '''
    
        # print("PATENT CITATION's Puras ==============")
        # print("Total -> ", len(pcs))
        # for p in pcs:
        #   print(" ===> ", p)
        # print("PATENT CITATION's Puras==============")

        return pcs
    except Exception as e:
        return 'No answer' + str(e)
x = ' Espécie: Proc. 23072.212827/2021-59 - Contrato de Partilhamento de Titularidade de Tecnologia e outras avenças que entre si celebram a Universidade Federal de Minas Gerais - UFMG - CNPJ nº 17.217.985/0001-04, por meio de sua Coordenadoria de Transferência e Inovação Tecnológica - CTIT, e a Odonto Tech Pesquisa E Inovação Ltda.- ODONTO TECH -CNPJ nº 34.711.535/0001-92. Objeto: Disciplinar as condições de partilhamento dos direitos de propriedade intelectual relativos à Tecnologia intitulada "Material Híbrido Nanoestruturado a base de Oligômeros de Nióbio, processo de obtenção e uso" consubstanciada no pedido de patente depositado junto ao Instituto Nacional de Propriedade Industrial - INPI sob o número BR 1020200163620 em 11/08/2020. Início da'
print(cnpj(x))