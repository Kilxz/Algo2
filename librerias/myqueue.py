from algo1 import *
from mystack import *
from mylinkedlist import *

def enqueue(Q, element):
  add(Q, element)
  return element
  
def dequeue(Q):
  long = length(Q)
  currentNode = Q.head
  if Q.head == None:
    return None

  elif long == 1:
    element = Q.head.value
    Q.head = None
    return element
    
  else:
    for i in range (0,long):
    
      if i == long-2:
        element = currentNode.nextNode.value
        currentNode.nextNode = None
        return element
      
      currentNode = currentNode.nextNode
    
