
def asiganarV(cadena,posicion):
      cadena=list(cadena)
      if cadena[posicion]=='0':
            cadena[posicion]='Z'
            if cadena[posicion+1]=='0':
                  print("A")
                  cadena[posicion+1]='Z'
                  return cambiar2(cadena,'B',posicion+2)
      if cadena[posicion]=='1':
            print("B")

def cambiar2(cadena,variable,posicion):
      lista=list(cadena)
      posicion=posicion+3;
      for j in range(4):
            if lista[posicion-j]=='1':
                  lista[posicion-j]='Y'
                  for i in range(len(lista)):
                        if lista[i]==variable:
                              lista[i-1-j]='Y'
            if lista[posicion-j]=='0':
                  lista[posicion-j]='X'
                  for i in range(len(lista)):
                        if lista[i]==variable:
                              lista[i-1-j]='X'
      return cambiar(lista) 
    
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