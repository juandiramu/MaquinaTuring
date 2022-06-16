from operator import le
from re import A
from asignarValor import *;
from desplazar import desplazar;
from asignarVariable import asignarVariable;

def ignorar(cadena, posicion):
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
                    break;
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
                    return asiganarV(cadena2,i+1)
                if cadena[i]=="1":
                    cadena2[i]='Z'
                    print("Asignar Variable")
                    return asignarVariable(cadena2,i)
            if cadena[i]=="1":
                cadena2[i]='Z'
                i+=1;
                if cadena[i]=="0":
                    cadena2[i]='Z'
                    print("Desplazar")
                    return desplazar(cadena2,i+1)
                if cadena[i]=="1":
                    print("Sumar")
                    break;

def inicio(lista):
    for i in range(len(lista)):
      if cadena[i]=="S":
        return(ignorar(cadena,i))

cadena="A0111B0111C0000T0000S010011111"
lista= list(cadena)
print(lista)
otra=inicio(lista)
print(otra)
        


          