from asignarValor import *;
from desplazar import desplazar;
from asignarVariable import asignarVariable;
from inicioRepetir import repetir;
from complementoA2 import complementoA2

def ignorar(cadena, posicion):
    cadena2=list(cadena)
    for i in range(posicion+1,len(cadena2)):
        if cadena[i]=="1":
            cadena2[i]='Z'
            i+=1;
            if cadena[i]=="0":
                cadena2[i]='Z'
                i+=1;
                if cadena[i]=="0":
                    cadena2[i]='Z'
                    print("Complemento A2")
                    return complementoA2(cadena2,i+1)
                if cadena[i]=="1":
                    cadena2[i]='Z'
                    print("Inicio Repetir")
                    return repetir(cadena2)
            elif cadena[i]=="1":
                print(cadena[i])
                i+=1;
                print(cadena[i])
                if cadena[i]=="0":
                    print("Fin repetir")
                    break;
                if cadena[i]=="1":
                    print("Fin Programa")
                    return 'heloi';
        elif cadena[i]=="0":
            cadena2[i]='Z'
            i+=1;
            if cadena[i]=="0":
                cadena2[i]='Z'
                i+=1;
                if cadena[i]=="0":
                    cadena2[i]='Z'
                    print("Asignar Valor")
                    asiganarV(cadena2,i+1)
                if cadena[i]=="1":
                    cadena2[i]='Z'
                    print("Asignar Variable")
                    print(asignarVariable(cadena2,i))
            elif cadena[i]=="1":
                cadena2[i]='Z'
                i+=1;
                if cadena[i]=="0":
                    cadena2[i]='Z'
                    print("Desplazar")
                    print(desplazar(cadena2,i+1))
                if cadena[i]=="1":
                    print("Sumar")
                    break;

def inicio(lista):
    for i in range(len(lista)):
      if lista[i]=="S":
          (ignorar(lista,i))
    return lista

cadena="A0111B0111C0100T0111S10011111"
lista= list(cadena)
print(lista)
otra=inicio(lista)
print(otra)
        


          