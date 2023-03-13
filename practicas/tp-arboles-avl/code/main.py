from avltree import *

A = AVLTree()

insert(A, 10, 10)
insert(A, 4, 4)
insert(A, 3, 3)
insert(A, 15, 15)
insert(A, 2, 2)

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
insert(B, 10, 10)
insert(B, 4, 4)
insert(B, 3, 3)
insert(B, 15, 15)
insert(B, 2, 2)

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
insert(C, 10, 10)
insert(C, 4, 4)
insert(C, 15, 15)
C = reBalance(C)
print(B.root.value)
print(B.root.rightnode.value)
print(B.root.leftnode.value)