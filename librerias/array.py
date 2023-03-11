from algo1 import *

def search(Array, element):
  posicion = -1
  contador = 0
  while (posicion == -1):
    if element == Array[contador]:
      posicion = contador
    if (contador == len(Array)-1):
      posicion = None
    contador = contador + 1
  return posicion

#Se valida que la posición sea mayor que 0 antes de llamar a la función
def insert(Array, element, position):
  if position < len(Array):
    if Array[position] != None:
      dim = len(Array)
      for i in range(dim-1, position, -1):
        Array[i] = Array[i-1]
      Array[position] = element
    
    else:
      Array[position] = element
      
  else:
    position = None
  return position

def delete(Array,element):
  posicion = search(Array, element)
  if posicion != None:
    for i in range(posicion, len(Array)-1):
      Array[i] = Array[i+1]
    Array[len(Array)-1] = None
  return posicion

def length(Array):
  long=0
  for i in range(0, len(Array)):
    if Array[i] != None:
      long=long+1
  return long
      