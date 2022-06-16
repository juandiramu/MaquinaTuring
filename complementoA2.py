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
    j=len(cadena)-1
    for i in range(len(cadena)):
        if cadena[j-i]==variable:
            print
