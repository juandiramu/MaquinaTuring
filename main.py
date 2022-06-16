from operator import le
from re import A
from asignarValor import *;
from asignarVariable import asignarVariable;

def ignorar(cadena, posición):
    cadena2=list(cadena)
    for i in range(len(cadena)):
        if i>posición and cadena[i]=="1":
            i+=1;
            if cadena[i]=="0":
                i+=1;
                if cadena[i]=="0":
                    print("Complemento A2")
                    break;
                if cadena[i]=="1":
                    print("Inicio Repetir")
                    break;
            if cadena[i+1]=="1":
                i+=1;
                if cadena[i]=="0":
                    print("Fin repetir")
                    break;
                if cadena[i]=="1":
                    print("Fin Programa")
                    break;
        if i>posición and cadena[i]=="0":
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
            if cadena[i+1]=="1":
                i+=1;
                if cadena[i]=="0":
                    print("Desplazar")
                    break;
                if cadena[i]=="1":
                    print("Sumar")
                    break;

def inicio(lista):
    for i in range(len(lista)):
      if cadena[i]=="S":
        print(ignorar(cadena,i))

cadena="A0000B0000C0000T0000S000000011"
lista= list(cadena)
print(lista)
inicio(lista)

        


          