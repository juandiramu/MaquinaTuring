from automata import automata;

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
                    return asignarValor(cadena2,i)
                if cadena[i]=="1":
                    print("Asignar Variable")
                    break;
            if cadena[i+1]=="1":
                i+=1;
                if cadena[i]=="0":
                    print("Desplazar")
                    break;
                if cadena[i]=="1":
                    print("Sumar")
                    break;

def asignarValor(cadena,pocision):
    cadena2=list(cadena)
    cadena2[pocision]='Z'
    pocision+=1; 
    if cadena[pocision]=="0":
        cadena2[pocision]='Z'
        pocision+=1;
        if cadena[pocision]=="0":
           cadena2[pocision]='Z'
           print("A")
           pocision+=3
           if cadena[pocision]=="0":
                print("Cambiar a A 0")
                return;
           if cadena[pocision]=="1":
                print("Cambiar a A 1")
                cadena2[pocision+1]='Z'
                return cadena2
        if cadena[pocision]=="1":
           print("B")
    elif cadena[pocision]=="1":
        pocision+=1;
        if cadena[pocision]=="0":
           print("C")
        if cadena[pocision]=="1":
           print("T")
cadena="A0000B0000COOOOTOOOOS000001011"
lista= list(cadena)
for i in range(len(lista)):
    if cadena[i]=="S":
     print(ignorar(cadena,i))
        


          