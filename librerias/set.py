from algo1 import *

def check_duplicates(Array):
  dim = len(Array)
  verificacion = True
  for i in range(0, dim - 1):
    if verificacion != False:
      for j in range(i + 1, dim):
        if (verificacion != False) and (Array[i] == Array[j]):
          verificacion = False
          print("Existen elementos repetidos en el Array")
  return verificacion
  
def Create_Set(array):
  n = len(array)

  for i in range (0, n-1):
    for j in range(i + 1, n):
      if array[i] != None:
        if array[i] == array[j]:
          array[j] = None

  contador = 0
  for i in range(0, n):
    if array[i] == None:
      contador = contador + 1

  m = n - contador

  vectoracortado = Array(m, 0)
  cont = 0
  for i in range(0, n):
    if array[i] != None:
      vectoracortado[cont] = array[i]
      cont = cont + 1

  return vectoracortado
  
def Union(arrayS, arrayT):
  
  if check_duplicates(arrayS) == False:
    arrayS = Create_Set(arrayS)
  if check_duplicates(arrayT) == False:
    arrayT = Create_Set(arrayT)
    
  dim1 = len(arrayS)
  dim2 = len(arrayT)
  dim_union = dim1 + dim2
  vectorunion = Array(dim_union, 0)
  contador = 0
  
  for i in range(0, dim_union):
    if i <= (dim1 - 1):
      vectorunion[i] = arrayS[i]
    else:
      vectorunion[i] = arrayT[contador]
      contador = contador + 1
      
  vectorunion = Create_Set(vectorunion)
  return vectorunion

def Intersection(arrayS, arrayT):
  if check_duplicates(arrayS) == False:
    arrayS = Create_Set(arrayS)
  if check_duplicates(arrayT) == False:
    arrayT = Create_Set(arrayT)
    
  dim1 = len(arrayS)
  dim2 = len(arrayT)
  contador = 0
  
  for i in range(0, dim1):
    for j in range(0, dim2):
      if arrayS[i] == arrayT[j]:
        contador = contador + 1
  vectorinterseccion = Array(contador, 0)
  contador = 0
  
  for i in range(0, dim1):
    for j in range(0, dim2):
      if arrayS[i] == arrayT[j]:
        vectorinterseccion[contador] = arrayS[i]
        contador = contador +1
  return vectorinterseccion

def Difference(arrayS, arrayT):
  
  if check_duplicates(arrayS) == False:
    arrayS = Create_Set(arrayS)
  if check_duplicates(arrayT) == False:
    arrayT = Create_Set(arrayT)
    
  dim1 = len(arrayS)
  dim2 = len(arrayT)

  contador = 0
  for i in range(0, dim1):
    for j in range(0, dim2):
      if arrayS[i] != None:
        if arrayS[i] == arrayT[j]:
          arrayS[i] = None
          contador = contador + 1
          
  vectordiferencia = Array(dim1-contador, 0)
  contador = 0
  for i in range(0, dim1):
    if arrayS[i] != None:
      vectordiferencia[contador] = arrayS[i]
      contador = contador + 1
  return vectordiferencia
        