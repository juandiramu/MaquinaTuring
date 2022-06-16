
def ignorarAv(cadena,semaforo):
        tamaño=len(cadena)-1;
        for i in range(tamaño):
          if cadena[tamaño-i]==semaforo:
             return tamaño-i-1;

def asignar(cadena):
        tamaño=len(cadena)-1;
        bandera=0
        for i in range(tamaño):
          if cadena[tamaño-i]=='B':
                bandera=tamaño-i;
          if (cadena[tamaño-i]=='1' or cadena[tamaño-i]=='0')and bandera!=0 and bandera!=tamaño-i:
                return tamaño-i
        

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
              pocision+=4;
              if cadena2[pocision]=="1":
                    cadena2[pocision]="Y"
                    l=ignorarAv(cadena2,"B");
                    cadena2[l]="Y"
                    bandera=0
                    for j in range(3):
                     for i in range(len(cadena2)):
                      if cadena2[i]=='S':
                            bandera=i;
                      if (cadena2[i]=="Y" or cadena2[i]=="X") and i>bandera and bandera!=0:
                            if(cadena2[i-1]=='1'):
                                cadena2[i-1]='Y'
                                cadena2[asignar(cadena2)]='Y';                     
                            if(cadena2[i-1]=='0'):
                                cadena2[i-1]='X'
                                cadena2[asignar(cadena2)]='X';                     
                    return cambiar(cadena2);
              if cadena2[pocision]=="0":
                    cadena2[pocision]="X"
                    l= ignorarAv(cadena2,"B");
                    cadena2[l]="X"
                    bandera=0
                    for i in range(3):
                        for i in range(l,len(cadena2)):
                         if cadena2[i]=='S':
                                bandera=i;
                         if (cadena2[i]=="Y" or cadena2[i]=="X") and i>bandera and bandera!=0:
                                if(cadena2[i-1]=='1'):
                                    cadena2[i-1]='Y'
                                if(cadena2[i-1]=='0'):
                                    cadena2[i-1]='X'
                    
                    return cambiar(cadena2)
              if cadena2[pocision]=='0':
                    cadena2[pocision]="Z"
                    l= ignorarAv(cadena2,"B");
                    cadena2[l]="X"
                    return cadena2;
            if cadena[pocision]=="1":
              print("B")
        elif cadena[pocision]=="1":
            pocision+=1;
            if cadena[pocision]=="0":
              print("C")
            if cadena[pocision]=="1":
              print("T")

def cambiar(cadena):
  for i in range(len(cadena)):
    cadena=list(cadena)
    if cadena[i]=="X":
          cadena[i]='0'
    if cadena[i]=="Y":
          cadena[i]='1'
    if cadena[i]=="S":
          break;
  return cadena