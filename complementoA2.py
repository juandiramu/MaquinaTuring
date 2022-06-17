def complementoA2(cadena,posicion):
    lista=list(cadena);
    if lista[posicion]=='0':
            lista[posicion]='Z'
            if lista[posicion+1]=='0':
                  print("A")
                  lista[posicion+1]='Z'
                  return calculo(lista,'B')
            if lista[posicion+1]=='1':
                  print("B")
                  lista[posicion+1]='Z'
                  return calculo(lista,'C')
    if lista[posicion]=='1':
            lista[posicion]='Z'
            if lista[posicion+1]=='0':
                  print("C")
                  lista[posicion+1]='Z'
                  return calculo(lista,'T')
            if lista[posicion+1]=='1':
                  print("T")
                  lista[posicion+1]='Z'
                  return calculo(lista,'S')

def calculo(cadena,variable):
    cadena=list(cadena)
    for i in range(len(cadena)):
        if cadena[i]==variable:
            if cadena[i-1]=='0' and cadena[i-2]=='0' and cadena[i-3]=='0' and cadena[i-4]=='0':
                  return cadena
            if cadena[i-1]=='1':
                  for k in range(1,4):
                        if cadena[i-1-k]=="1":
                              cadena[i-1-k]='0'
                        elif cadena[i-1-k]=='0':
                              cadena[i-1-k]='1'
                  return cadena
            if cadena[i-2]=='1':
                  for k in range(1,3):
                        if cadena[i-1-k]=='1':
                              cadena[i-1-k]='0'
                        elif cadena[i-1-k]=='0':
                              cadena[i-1-k]='1'
                  return cadena
            if cadena[i-3]=='1':
                  for k in range(1,2):
                        if cadena[i-1-k]=='1':
                              cadena[i-1-k]='0'
                        elif cadena[i-1-k]=='0':
                              cadena[i-1-k]='1'
            if cadena[i-4]=='1':
                  for k in range(1,1):
                        if cadena[i-1-k]=='1':
                              cadena[i-1-k]='0'
                        elif cadena[i-1-k]=='0':
                              cadena[i-1-k]='1'
            