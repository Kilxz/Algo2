from avltree import *

A = AVLTree()

insertAVL(A, 10, 10)
insertAVL(A, 4, 4)
insertAVL(A, 3, 3)
insertAVL(A, 15, 15)
insertAVL(A, 2, 2)

print(A.root.value)
print(A.root.rightnode.value)
print(A.root.leftnode.value)

print("Primer calculateBalance")
A = calculateBalance(A)
print(A.root.bf)
print(A.root.rightnode.bf)
print(A.root.leftnode.bf)
print(A.root.leftnode.leftnode.bf)
print(A.root.leftnode.leftnode.leftnode.bf)




print("Rotacion derecha:")
rotateRight(A, A.root)
print(A.root.value)
print(A.root.rightnode.value)
print(A.root.rightnode.rightnode.value)
print(A.root.leftnode.value)
print(A.root.leftnode.leftnode.value)
print(A.root.leftnode.rightnode)
print(A.root.leftnode.leftnode.rightnode)
print(A.root.rightnode.leftnode)
print(A.root.rightnode.rightnode.leftnode)


print("Segundo calculateBalance")
A = calculateBalance(A)
print(A.root.bf)
print(A.root.rightnode.bf)
print(A.root.rightnode.rightnode.bf)
print(A.root.leftnode.bf)
print(A.root.leftnode.leftnode.bf)

print("ARBOL B")
B = AVLTree()
insertAVL(B, 10, 10)
insertAVL(B, 4, 4)
insertAVL(B, 3, 3)
insertAVL(B, 15, 15)
insertAVL(B, 2, 2)

print("rebalance B")
reBalance(B)

print(B.root.value)
print(B.root.rightnode.value)
print(B.root.rightnode.rightnode.value)
print(B.root.leftnode.value)
print(B.root.leftnode.leftnode.value)
print(B.root.leftnode.rightnode)
print(B.root.leftnode.leftnode.rightnode)
print(B.root.rightnode.leftnode)
print(B.root.rightnode.rightnode.leftnode)

print("Rebalance arbol balanceado")
C = AVLTree()
insertAVL(C, 10, 10)
insertAVL(C, 4, 4)
insertAVL(C, 15, 15)
C = reBalance(C)
print(B.root.value)
print(B.root.rightnode.value)
print(B.root.leftnode.value)


print("Prueba insert")
D = AVLTree()
insert(D, 10, 10)
insert(D, 4, 4)
insert(D, 3, 3)
insert(D, 15, 15)
insert(D, 2, 2)

print(D.root.value)
print(D.root.rightnode.value)
print(D.root.rightnode.rightnode.value)
print(D.root.leftnode.value)
print(D.root.leftnode.leftnode.value)
print(D.root.leftnode.rightnode)
print(D.root.leftnode.leftnode.rightnode)
print(D.root.rightnode.leftnode)
print(D.root.rightnode.rightnode.leftnode)


print("Prueba delete")
E = AVLTree()
insertAVL(E, 4, 4)

insertAVL(E, 10, 10)

insertAVL(E, 3, 3)
insertAVL(E, 15, 15)
insertAVL(E, 2, 2)
insertAVL(E, 1, 1)

delete(E, 15)

print(E.root.value)
print(E.root.rightnode.value)
print(E.root.rightnode.rightnode.value)
print(E.root.leftnode.value)
print(E.root.leftnode.leftnode.value)
print(E.root.leftnode.rightnode)
print(E.root.leftnode.leftnode.rightnode)
print(E.root.rightnode.leftnode)
print(E.root.rightnode.rightnode.leftnode)

print("CASO ESPECIAL DE ROTACION")

F = AVLTree()
insertAVL(F, -2, -2)
insertAVL(F, 1, 1)
insertAVL(F, 0, 0)
print("Arbol sin balancear: ")
print(F.root.value)
print(F.root.rightnode.value)
print(F.root.rightnode.leftnode.value)

print("Arbol balanceado: ")
F = reBalance(F)
print(F.root.value)
print(F.root.rightnode.value)
print(F.root.leftnode.value)