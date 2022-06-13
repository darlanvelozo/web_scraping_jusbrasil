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