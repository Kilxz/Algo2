from mylinkedlist import *
from algo1 import *

class LinkedList:
  head = None
  
class Node:
  value = None
  nextNode = None

def push(S, element):
  add(S, element)
  return element

def pop(S):
  if S.head != None:
    currentNode = S.head.nextNode
    element = S.head.value
    S.head.nextNode = None
    S.head = currentNode
    return element
  else:
    return None