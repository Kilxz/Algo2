class AVLTree:
  root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None


def rotateLeft(Tree, avlnode):

#Caso si el nodo es la raíz de todo el árbol
  if Tree.root == avlnode:
    Tree.root = avlnode.rightnode
    Tree.root.parent = None
    if Tree.root.leftnode != None:
      avlnode.rightnode = Tree.root.leftnode
      Tree.root.leftnode.parent = avlnode
    Tree.root.leftnode = avlnode
    avlnode.parent = Tree.root
    return Tree
    
  #Verifico si el nodo esta a la derecha o a la izquierda del padre
  if avlnode.parent.rightnode == avlnode:
    padreHijo = "right"
  else:
    padreHijo = "left"

  #Inserto la nueva raiz dependiendo de PadreHijo
    avlnode.rightnode.parent = avlnode.parent
  if padreHijo == "right":
    avlnode.parent.rightnode = avlnode.rightnode
  else:
    avlnode.parent.leftnode = avlnode.rightnode
  #Si tiene hijo izquierdo, pasa a ser el hijo derecho de la antigua raiz. Posteriormente, la antigua raiz se inserta a la izquierda de la nueva raíz.
  newRoot = avlnode.rightnode
  if newRoot.leftnode != None:
    avlnode.rightnode = newRoot.leftnode
    newRoot.leftnode.parent = avlnode
  newRoot.leftnode = avlnode
  avlnode.parent = newRoot
  return Tree

def rotateRight(Tree, avlnode):
#Caso si el nodo es la raíz de todo el árbol
  if Tree.root == avlnode:
    Tree.root = avlnode.leftnode
    Tree.root.parent = None
    if Tree.root.rightnode != None:
      avlnode.leftnode = Tree.root.rightnode
      Tree.root.rightnode.parent = avlnode
    Tree.root.rightnode = avlnode
    avlnode.parent = Tree.root
    return Tree
    
  #Verifico si el nodo esta a la derecha o a la izquierda del padre
  if avlnode.parent.rightnode == avlnode:
    padreHijo = "right"
  else:
    padreHijo = "left"

  #Inserto la nueva raiz dependiendo de PadreHijo
    avlnode.leftnode.parent = avlnode.parent
  if padreHijo == "right":
    avlnode.parent.rightnode = avlnode.leftnode
  else:
    avlnode.parent.leftnode = avlnode.leftnode
  #Si tiene hijo derecho, pasa a ser el hijo izquierdo de la antigua raiz. Posteriormente, la antigua raiz se inserta a la derecha de la nueva raíz.
  newRoot = avlnode.leftnode
  if newRoot.rightnode != None:
    avlnode.leftnode = newRoot.rightnode
    newRoot.rightnode.parent = avlnode
  newRoot.rightnode = avlnode
  avlnode.parent = newRoot
  return Tree