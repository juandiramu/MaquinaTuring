def asignarVariable(lista,posicion):
    lista=list(lista)
    if lista[posicion+1]=='0':
        lista[posicion+1]='Z'
        if lista[posicion+2]=='0':
            lista[posicion+2]='Z'
            if lista[posicion+3]=='0':
               lista[posicion+3]='Z'
               if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar A por A')
                    return lista
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar A por B')
                    return cambiar("B","C",lista)
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar A por C')
                    return cambiar("B","T",lista)
                if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar A por T')
                    return cambiar("B","S",lista)
        if lista[posicion+2]=='1':
            lista[posicion+2]='Z'
            if lista[posicion+3]=='0':
               lista[posicion+3]='Z'
               if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar B por A')
                    return cambiar("C","B",lista)
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar B por B')
                    return lista
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar B por C')
                    return cambiar("C","T",lista)
                if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar B por T')
                    return cambiar("C","S",lista)
    if lista[posicion+1]=='1':
        lista[posicion+1]='Z'
        if lista[posicion+2]=='0':
            lista[posicion+2]='Z'
            if lista[posicion+3]=='0':
               lista[posicion+3]='Z'
               if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar C por A')
                    return cambiar("T","B",lista)
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar C por B')
                    return cambiar("T","C",lista)
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar C por C')
                    return lista
                if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar C por T')
                    return cambiar("T","S",lista)
        if lista[posicion+2]=='1':
            lista[posicion+2]='Z'
            if lista[posicion+3]=='0':
               lista[posicion+3]='Z'
               if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar T por A')
                    return cambiar("S","B",lista)
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar T por B')
                    return cambiar("S","C",lista)
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar T por C')
                    return cambiar("S","T",lista)
                if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar T por T')
                    return lista

def cambiar(cambiar, nueva,lista):
    lista=list(lista);
    bandera=0
    for i in range(len(lista)):
        if lista[i]==nueva:
            bandera=i
    for j in range(1,5):
        if lista[bandera-j]=='1':
            lista[bandera-j]='Y'
            for k in range(len(lista)):
                if lista[k]==cambiar:
                    lista[k-j]='Y'
        if lista[bandera-j]=='0':
            lista[bandera-j]='X'
            for k in range(len(lista)):
                if lista[k]==cambiar:
                    lista[k-j]='X'
    return cambiar2(lista)

def cambiar2(cadena):
  for i in range(len(cadena)):
    cadena=list(cadena)
    if cadena[i]=="X":
          cadena[i]='0'
    if cadena[i]=="Y":
          cadena[i]='1'
    if cadena[i]=="S":
          break;
  return cadena

            

     
                    
