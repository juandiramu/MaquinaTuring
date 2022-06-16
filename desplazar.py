def desplazar(cadena,posicion):
      cadena=list(cadena)
      if cadena[posicion]=='0':
            cadena[posicion]='Z'
            if cadena[posicion+1]=='0':
                  print("A")
                  cadena[posicion+1]='Z'
                  if cadena[posicion+2]=='0':
                    cadena[posicion+2]='Z'  
                    return desplazarI(cadena,'A')
                  if cadena[posicion+2]=='1':
                        cadena[posicion+2]='Z'
                        return desplazarD(cadena,'A')
            if cadena[posicion+1]=='1':
                  print("B")
                  cadena[posicion+1]='Z'
                  if cadena[posicion+2]=='0':
                        cadena[posicion+2]='Z'
                        return desplazarI(cadena,'B')
                  if cadena[posicion+2]=='1':
                        cadena[posicion+2]='Z'
                        return desplazarD(cadena,'C')
      if cadena[posicion]=='1':
            cadena[posicion]='Z'
            if cadena[posicion+1]=='0':
                  print("C")
                  cadena[posicion+1]='Z'
                  if cadena[posicion+2]=='0':
                        cadena[posicion+2]='Z'
                        return desplazarI(cadena,'C')
                  if cadena[posicion+2]=='1':
                        cadena[posicion+2]='Z'
                        return desplazarD(cadena,'C')
            if cadena[posicion+1]=='1':
                  print("T")
                  cadena[posicion+1]='Z'
                  if cadena[posicion+2]=='0':
                        cadena[posicion+2]='Z'
                        return desplazarI(cadena,'T')
                  if cadena[posicion+2]=='1':
                        cadena[posicion+2]='Z'
                        return desplazarD(cadena,'T')

def desplazarI(lista,variable):
    lista=list(lista);
    bandera=0
    b2=0
    for j in range(3):
        for i in range(len(lista)):
            if lista[i]==variable:
                bandera=lista[i+2+j]
                lista[i+1+j]=bandera;
                b2=i+2+j
    lista[b2]='0'
    return lista

def desplazarD(lista,variable):
    print("Desplazar a la derecha")
    lista=list(lista);
    bandera=0
    b2=0
    for j in range(3):
        for i in range(len(lista)):
            if lista[i]==variable:
                bandera=lista[i-2-j]
                lista[i-1-j]=bandera;
                b2=i-2-j
    lista[b2]='0'
    return lista



