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
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar B por B')
                    return lista
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar B por C')
                if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar B por T')
    if lista[posicion+1]=='1':
        lista[posicion+1]='Z'
        if lista[posicion+2]=='0':
            lista[posicion+2]='Z'
            if lista[posicion+3]=='0':
               lista[posicion+3]='Z'
               if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar C por A')
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar C por B')
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar C por C')
                    return lista
                if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar C por T')
        if lista[posicion+2]=='1':
            lista[posicion+2]='Z'
            if lista[posicion+3]=='0':
               lista[posicion+3]='Z'
               if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar T por A')
               if lista[posicion+4]=='1':
                    lista[posicion+4]='Z'
                    print('Cambiar T por B')
            if lista[posicion+3]=='1':
                lista[posicion+3]='Z'
                if lista[posicion+4]=='0':
                    lista[posicion+4]='Z'
                    print('Cambiar T por C')
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
    return lista



            

     
                    
