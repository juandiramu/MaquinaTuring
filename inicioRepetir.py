def repetir(cadena):
    for i in range(len(cadena)):
        if cadena[i]=='C':
            if cadena[i+1]=='0' and cadena[i+2]=='0' and cadena[i+3]=='0' and cadena[i+4]=='0':
                print('0 en la variable C')
                return ignorar(cadena)
            else:
                print('debe repetirse varias veces')

def ignorar(cadena):
    cadena=list(cadena)
    bandera=-1
    for i in range(len(cadena)):
        if cadena[i]=='S':
            bandera=i
        if (cadena[i]=='1' or cadena[i]=='0') and ((i-bandera)<=3
         and bandera !=-1):
            cadena[i]='Z'
        if (i-bandera)>3 and bandera !=-1:
            return ignorar2(cadena,i)
    return cadena

def ignorar2(cadena,posicion):
    cadena2=list(cadena)
    for i in range(posicion,len(cadena)):
        if cadena[i]=="1":
            print(cadena[i])
            i+=1;
            if cadena[i]=="0":
                i+=1;
                if cadena[i]=="0":
                    print("Complemento A2")
                    break;
                if cadena[i]=="1":
                    print("Inicio Repetir")
                    break
            if cadena[i]=="1":
                print(cadena[i])
                i+=1;
                print(cadena[i])
                if cadena[i]=="0":
                    print("Fin repetir")
                    break;
                if cadena[i]=="1":
                    print("Fin Programa")
                    return 'heloi';
        if cadena[i]=="0":
            cadena2[i]='Z'
            i+=1;
            if cadena[i]=="0":
                cadena2[i]='Z'
                i+=1;
                if cadena[i]=="0":
                    cadena2[i]='Z'
                    print("Asignar Valor")
                    break
                if cadena[i]=="1":
                    cadena2[i]='Z'
                    print("Asignar Variable")
                    break
            if cadena[i]=="1":
                cadena2[i]='Z'
                i+=1;
                if cadena[i]=="0":
                    cadena2[i]='Z'
                    print("Desplazar")
                    break
                if cadena[i]=="1":
                    print("Sumar")
                    break;
