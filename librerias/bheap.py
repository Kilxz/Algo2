import mylinkedlist
from random import randint

class Bheap:
    """ Estructura Bheap, lo unico que tiene una referencia a un lista.
    """
    bheaplist=mylinkedlist.LinkedList()
    def __str__(self):
            """ Permite hacer un print a una estructura Bheap
            """
            str_list=""
            current=self.bheaplist.head.nextNode
            while current!=None:
                str_list= str_list+str(current.value)+" "
                current=current.nextNode
            return(str_list)



def delMax(BH):
  """ Recupera el mayor elemento del heap. Este siempre se encontrara al comienzo (posicion 1).
        Para manter la esctrucura del arbol binario se reemplaza el nodo raiz por el ultimo nodo.
        
        Luego mediante la funcion shiftDown se va recorriendo el arbol hasta encontrar la posicion 
        correcta de dicho nodo. De esta manara se garantiza la propiedad heap.
  """
  if mylinkedlist.length(BH.bheaplist) > 1:
    retval = mylinkedlist.accessNode(BH.bheaplist, 1)
    auxnode = mylinkedlist.dequeueNode(BH.bheaplist)
    mylinkedlist.insertNode(BH.bheaplist, auxnode, 1)
    mylinkedlist.delete(BH.bheaplist, retval.value)
    shiftDown(BH, 1)
    return retval


def shiftUp(BH,i):
    """ Recorre el arbol desde los nodos hacia la raiz y va reemplazando el nodo i por su padre
        siempre y cuando i sea mayor. La operacion matematica i // 2 nos permite rapidamente encontrar al padre.
    """
    while i // 2 > 0:
      j = i // 2
      if mylinkedlist.access(BH.bheaplist, j) < mylinkedlist.access(BH.bheaplist, i):
        aux = mylinkedlist.accessNode(BH.bheaplist,i)
        aux2 = mylinkedlist.accessNode(BH.bheaplist, j)
        mylinkedlist.delete(BH.bheaplist, mylinkedlist.access(BH.bheaplist, i))
        mylinkedlist.delete(BH.bheaplist, mylinkedlist.access(BH.bheaplist, j))
        mylinkedlist.insertNode(BH.bheaplist, aux, j)
        mylinkedlist.insertNode(BH.bheaplist, aux, i)
      
      i = i // 2
    shiftUp(BH, i-1)

def shiftDown(BH,i,currentsize=None):
    """ Recorre el arbol desde la raiz y  hacia los nodos (arriba hacia abajo) va reemplazando el nodo i por sus hijos
        siempre y cuando alguno de sus hijos sea mayor. 
    """
    if currentsize==None:
        currentsize=mylinkedlist.length(BH.bheaplist)-1
    while (i * 2) <= currentsize:
      mc = maxChild(BH,i,currentsize)
      uno = mylinkedlist.access(BH.bheaplist, i)
      dos = mylinkedlist.access(BH.bheaplist, mc)
      if dos != None and uno < dos:
        aux = mylinkedlist.accessNode(BH.bheaplist, i)
        aux2 = mylinkedlist.accessNode(BH.bheaplist, mc)
        mylinkedlist.delete(BH.bheaplist, mylinkedlist.access(BH.bheaplist, mc))
        mylinkedlist.delete(BH.bheaplist, mylinkedlist.access(BH.bheaplist, i))
        mylinkedlist.insertNode(BH.bheaplist, aux2, i)
        mylinkedlist.insertNode(BH.bheaplist, aux, mc)
        
      i = mc
      currentsize = currentsize-1
      shiftDown(BH, i, currentsize)

def maxChild(BH,i,currentsize):
    """ Determina dado un nodo i, cual de sus hijos es el mayor y devuelve la posicion 
    """
    if i * 2 + 1 > currentsize:
        return i * 2
    else:
        if mylinkedlist.access(BH.bheaplist,i*2) > mylinkedlist.access(BH.bheaplist,i*2+1):
            return i * 2 
        else:
            return i * 2 + 1
    
def insert(BH,k):
    """ Inserta un elemento en el heap. Si la lista esta vacia, se crea un elemento 0. Este ultimo no se utiliza,
        pero facilita las operaciones matematicas para acceder a los padres e hijos. 
    """
    pos=mylinkedlist.length(BH.bheaplist)
    if pos==0:
        mylinkedlist.add(H.bheaplist,0)
        pos=pos+1
    mylinkedlist.insert(BH.bheaplist,k,pos)
    currentsize=mylinkedlist.length(BH.bheaplist)-1
    shiftUp(BH,currentsize)

def heapify(BH,L):
    """ Dada una lista crea un heap con complejidad temporal O(n)
    
    """
    i = mylinkedlist.length(L) // 2
    BH.bheaplist.head = L.head 
    mylinkedlist.add(BH.bheaplist,0)
    while (i > 0):
        shiftDown(BH,i)
        i = i - 1
def length(BH):
    return mylinkedlist.length(BH.bheaplist)-1

def HeapSort(L):
  if L.head == None:
    return None
  BH = Bheap()
  heapify(BH, L)
  L.head = None
  HeapSortR(BH, L, mylinkedlist.length(BH.bheaplist))
  return L
  
def HeapSortR(BH, L, len):

  maxNode = delMax(BH)
  mylinkedlist.addNodeAtBegining(L, maxNode)
  shiftDown(BH, 1)
  if len > 2:
    HeapSortR(BH, L, len -1)
  return L
  
  
if __name__ == "__main__":
    H=Bheap()
    insert(H,8)
    insert(H,1)
    insert(H,5)
    insert(H,4)
    print(H)
    minimun=delMax(H)
    print(H)
    print("----")
    L=mylinkedlist.LinkedList()
    mylinkedlist.add(L,4)
    mylinkedlist.add(L,3)
    mylinkedlist.add(L,2)
    mylinkedlist.add(L,1)
    mylinkedlist.add(L,12)
    mylinkedlist.add(L,255)
    mylinkedlist.add(L,1000)
    print(L)
    heapify(H,L)
    print(H)