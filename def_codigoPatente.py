import re

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
                     '[A-Z][A-Z] \d\d \d{4} \d{7}']

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